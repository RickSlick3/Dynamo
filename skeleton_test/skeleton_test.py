import skeleton_test.skeleton_test as skeleton_test

if __name__ == "__main__":
    suite = unittest.findTestCases(skeleton_test)
    result = unittest.TestResult()
    suite.run(result, debug=True)
    print(f"{result=}")