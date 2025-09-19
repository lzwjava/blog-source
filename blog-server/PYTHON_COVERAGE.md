# Python Integration Tests with JaCoCo Coverage

This setup allows you to run Python integration tests against your Java server and generate accurate code coverage reports using JaCoCo.

## How it Works

Instead of attaching JaCoCo to the Python test runner, we attach it to the Java server process. This way, when Python tests make HTTP requests to your endpoints, the coverage data is collected in real-time.

## Quick Start

### 1. Run Python Integration Tests with Coverage

```bash
# Run all Python tests with JaCoCo coverage
mvn verify -P python-integration-tests

# Or run specific phases
mvn pre-integration-test -P python-integration-tests  # Start server with coverage
python -m unittest discover tests/ -v               # Run Python tests
mvn post-integration-test -P python-integration-tests # Stop server and generate report
```

### 2. View Coverage Report

After running tests, the coverage report will be available at:
```
target/site/jacoco-it/index.html
```

### 3. Manual Setup (Alternative)

If you want more control, you can manually start the server with JaCoCo:

```bash
# Download JaCoCo agent if not available
wget https://repo1.maven.org/maven2/org/jacoco/org.jacoco.agent/0.8.12/org.jacoco.agent-0.8.12-runtime.jar -O jacocoagent.jar

# Start server with JaCoCo agent
java -javaagent:jacocoagent.jar=destfile=jacoco-it.exec,output=file,append=false \
     -jar target/blog-server-1.0.jar

# In another terminal, run Python tests
python -m unittest discover tests/ -v

# Generate report after server stops
java -jar jacococli.jar report jacoco-it.exec --classfiles target/classes --sourcefiles src/main/java --html target/site/jacoco-it
```

## Test Configuration

### Environment Variables
- `TEST_SERVER_URL`: URL of the test server (default: http://localhost:8080)

### Test Structure
- Python tests should be in the `tests/` directory
- Tests use `unittest` framework
- Tests automatically wait for server startup

## Example Test

```python
import unittest
import requests

class TestMyAPI(unittest.TestCase):
    def test_endpoint(self):
        response = requests.get('http://localhost:8080/api/my-endpoint')
        self.assertEqual(response.status_code, 200)
```

## Troubleshooting

### Server Not Starting
- Check if port 8080 is available
- Verify Java process has JaCoCo agent attached
- Check logs in `target/spring.log`

### Coverage Not Collected
- Ensure tests are making actual HTTP requests (not mocked)
- Verify JaCoCo agent is properly attached to server
- Check `target/jacoco-it.exec` file is created

### Permission Issues
- Ensure Python has network access to localhost:8080
- Check firewall settings if running in containerized environment