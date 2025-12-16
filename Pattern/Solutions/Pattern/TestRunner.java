import java.io.*;
import java.nio.file.*;
import java.nio.file.StandardCopyOption;
import java.util.*;
import java.util.regex.*;

public class TestRunner {
    private static final String PATTERN_DIR = "d:\\gatetutor\\all Q\\Pattern";
    private static final String SOLUTIONS_DIR = "d:\\gatetutor\\all Q\\Solutions\\Pattern";
    
    public static void main(String[] args) {
        TestRunner runner = new TestRunner();
        runner.runAllTests();
    }
    
    public void runAllTests() {
        System.out.println("=== Pattern Problems Test Runner ===\n");
        
        int totalProblems = 0;
        int totalPassed = 0;
        int totalFailed = 0;
        
        for (int i = 1; i <= 30; i++) {
            String jsonFile = PATTERN_DIR + "\\" + i + ".json";
            File file = new File(jsonFile);
            
            if (!file.exists()) {
                System.out.println("Problem " + i + ": JSON file not found");
                continue;
            }
            
            try {
                String jsonContent = new String(Files.readAllBytes(file.toPath()));
                ProblemData problem = parseProblem(jsonContent, i);
                
                if (problem == null) {
                    System.out.println("Problem " + i + ": Failed to parse JSON");
                    continue;
                }
                
                totalProblems++;
                System.out.println("Problem " + i + ": " + problem.title);
                System.out.println("----------------------------------------");
                
                int passed = 0;
                int failed = 0;
                
                for (int tc = 0; tc < problem.testCases.size(); tc++) {
                    TestCase testCase = problem.testCases.get(tc);
                    boolean result = runTestCase(i, testCase);
                    
                    if (result) {
                        passed++;
                        System.out.println("  Test Case " + (tc + 1) + ": PASSED");
                    } else {
                        failed++;
                        System.out.println("  Test Case " + (tc + 1) + ": FAILED");
                        System.out.println("    Input: " + testCase.input);
                        System.out.println("    Expected: " + testCase.expectedOutput.replace("\n", "\\n"));
                        System.out.println("    Got: " + testCase.actualOutput.replace("\n", "\\n"));
                    }
                }
                
                System.out.println("  Summary: " + passed + " passed, " + failed + " failed out of " + problem.testCases.size());
                System.out.println();
                
                totalPassed += passed;
                totalFailed += failed;
                
            } catch (Exception e) {
                System.out.println("Problem " + i + ": Error - " + e.getMessage());
                e.printStackTrace();
                System.out.println();
            }
        }
        
        System.out.println("=== Overall Summary ===");
        System.out.println("Total Problems: " + totalProblems);
        System.out.println("Total Test Cases Passed: " + totalPassed);
        System.out.println("Total Test Cases Failed: " + totalFailed);
        System.out.println("Success Rate: " + (totalPassed * 100.0 / (totalPassed + totalFailed)) + "%");
    }
    
    private boolean runTestCase(int problemNum, TestCase testCase) {
        File tempDir = null;
        try {
            // Create a temporary directory for this test
            tempDir = Files.createTempDirectory("pattern_test_" + problemNum).toFile();
            tempDir.deleteOnExit();
            
            // Copy the Java file to temp directory
            String sourceFile = SOLUTIONS_DIR + "\\Problem" + problemNum + ".java";
            String className = "Problem" + problemNum;
            String destFile = tempDir.getAbsolutePath() + "\\" + className + ".java";
            Files.copy(Paths.get(sourceFile), Paths.get(destFile), StandardCopyOption.REPLACE_EXISTING);
            
            // Compile the Java file
            Process compileProcess = new ProcessBuilder("javac", destFile)
                .directory(tempDir)
                .redirectErrorStream(true)
                .start();
            
            String compileOutput = readProcessOutput(compileProcess);
            int compileExitCode = compileProcess.waitFor();
            
            if (compileExitCode != 0) {
                testCase.actualOutput = "COMPILATION ERROR: " + compileOutput;
                return false;
            }
            
            // Run the compiled class
            Process runProcess = new ProcessBuilder("java", className)
                .directory(tempDir)
                .redirectErrorStream(true)
                .start();
            
            // Write input to process
            PrintWriter writer = new PrintWriter(runProcess.getOutputStream());
            writer.println(testCase.input);
            writer.close();
            
            // Read output
            String output = readProcessOutput(runProcess);
            int exitCode = runProcess.waitFor();
            
            if (exitCode != 0) {
                testCase.actualOutput = "RUNTIME ERROR: " + output;
                return false;
            }
            
            // Normalize output (remove trailing newlines)
            output = output.trim();
            String expected = testCase.expectedOutput.trim();
            
            testCase.actualOutput = output;
            
            return output.equals(expected);
            
        } catch (Exception e) {
            testCase.actualOutput = "ERROR: " + e.getMessage();
            return false;
        } finally {
            // Clean up temp directory
            if (tempDir != null && tempDir.exists()) {
                deleteDirectory(tempDir);
            }
        }
    }
    
    private void deleteDirectory(File dir) {
        File[] files = dir.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    deleteDirectory(file);
                } else {
                    file.delete();
                }
            }
        }
        dir.delete();
    }
    
    private String readProcessOutput(Process process) throws IOException {
        StringBuilder output = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (output.length() > 0) {
                    output.append("\n");
                }
                output.append(line);
            }
        }
        return output.toString();
    }
    
    private ProblemData parseProblem(String json, int problemNum) {
        try {
            ProblemData problem = new ProblemData();
            
            // Extract title
            Pattern titlePattern = Pattern.compile("\"title\":\\s*\"([^\"]+)\"");
            Matcher titleMatcher = titlePattern.matcher(json);
            if (titleMatcher.find()) {
                problem.title = titleMatcher.group(1);
            }
            
            // Extract test cases
            Pattern testCasePattern = Pattern.compile(
                "\"testCases\":\\s*\\[(.*?)\\]", Pattern.DOTALL);
            Matcher testCaseMatcher = testCasePattern.matcher(json);
            
            if (testCaseMatcher.find()) {
                String testCasesStr = testCaseMatcher.group(1);
                
                // Extract individual test cases
                Pattern inputPattern = Pattern.compile("\"input\":\\s*\"([^\"]+)\"");
                Pattern outputPattern = Pattern.compile("\"expectedOutput\":\\s*\"((?:[^\"]|\\\\\")+)\"");
                
                String[] testCaseBlocks = testCasesStr.split("\\},\\s*\\{");
                
                for (String block : testCaseBlocks) {
                    TestCase tc = new TestCase();
                    
                    Matcher inputMatcher = inputPattern.matcher(block);
                    if (inputMatcher.find()) {
                        tc.input = inputMatcher.group(1);
                    }
                    
                    Matcher outputMatcher = outputPattern.matcher(block);
                    if (outputMatcher.find()) {
                        tc.expectedOutput = outputMatcher.group(1).replace("\\n", "\n");
                    }
                    
                    if (tc.input != null && tc.expectedOutput != null) {
                        problem.testCases.add(tc);
                    }
                }
            }
            
            return problem;
            
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    
    static class ProblemData {
        String title;
        List<TestCase> testCases = new ArrayList<>();
    }
    
    static class TestCase {
        String input;
        String expectedOutput;
        String actualOutput;
    }
}
