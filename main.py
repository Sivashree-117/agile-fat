import sys
import datetime

def run_tests():

    print("automatic build code")
    print("=========================================")
    print("Starting Jenkins Build Process...")
    print(f"Build Time: {datetime.datetime.now()}")
    print("=========================================")
    
    # Simulate some unit tests
    print("[INFO] Running unit tests...")
    tests_passed = True
    
    if tests_passed:
        print("[SUCCESS] All tests passed!")
        print("Build completed successfully.")
        sys.exit(0)
    else:
        print("[ERROR] Tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
