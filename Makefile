all:
	cmake . -B build/ -DCMAKE_BUILD_TYPE=Debug
	cmake --build build/

tests:
	cmake . -B build_tests/ -DCMAKE_BUILD_TYPE=Debug -DUNIT_TESTS=ON
	cmake --build build_tests/

clean:
	@rm -rf build
	@rm -rf build_tests
	@rm -rf binary
	@rm -rf unit_tests

.PHONY: all tests clean