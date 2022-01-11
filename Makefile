all:
	cmake . -B build/ -DCMAKE_BUILD_TYPE=Debug
	cmake --build build/

tests:
	cmake . -B build_tests/ -DCMAKE_BUILD_TYPE=Debug -DUNIT_TESTS=ON
	cmake --build build_tests/

clean:
	@rm -rf build
	@rm -rf QTranslator
	@rm -rf QTranslatorTests

.PHONY: all tests clean