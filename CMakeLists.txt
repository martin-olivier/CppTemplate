cmake_minimum_required(VERSION 3.17)

# Name of the CMake project
project(Template)

# C++ standard you want to use for the project
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_BINARY_DIR})

option(UNIT_TESTS "When sets to ON, build the unit tests" OFF)

if(UNIT_TESTS)
    # Bin name of the unit tests
    set(BIN unit_tests)
else()
    # Bin name of the project
    set(BIN binary)
endif()

# Fetch GoogleTest
if(UNIT_TESTS)
    find_package(googletest QUIET)
    include(FetchContent)
    FetchContent_Declare(
	    googletest
	    URL https://github.com/google/googletest/archive/refs/tags/release-1.11.0.zip
    )
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)
endif()

# Build flags
if(UNIX)
    add_compile_options(-Wall -Wextra -Weffc++)
elseif(WIN32)
    add_compile_options(/W4)
endif()

# Location of the main source file
set(MAIN src/main.cpp)

# List of source files
set(SOURCES
    # fill here
)

# List of tests source files
set(TEST_SOURCES
    tests/test.cpp
)

# Executable settings
if(UNIT_TESTS)
    add_executable(${BIN}
        ${SOURCES}
        ${TEST_SOURCES}
    )
    enable_testing()
    include(GoogleTest)
    gtest_discover_tests(${BIN})
    target_link_libraries(${BIN} PRIVATE gtest_main)
else()
    add_executable(${BIN}
        ${MAIN}
        ${SOURCES}
    )
endif()

# Include path of the project
target_include_directories(${BIN} PRIVATE include)