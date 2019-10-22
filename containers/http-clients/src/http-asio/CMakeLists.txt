cmake_minimum_required(VERSION 3.9)

set(CMAKE_EXPORT_COMPILE_COMMANDS 1)

FIND_PACKAGE(Boost 1.71.0 REQUIRED COMPONENTS system)

if(Boost_FOUND)
    INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS})
    LINK_DIRECTORIES(${Boost_LIBRARY_DIRS})
else()
    MESSAGE(FATAL_ERROR "Could not find Boost.")
endif()

FIND_PACKAGE(OpenSSL)

if (OPENSSL_FOUND)
    INCLUDE_DIRECTORIES(${OPENSSL_INCLUDE_DIR})
else()
    MESSAGE(FATAL_ERROR "Could not find OpenSSL.")
endif ()

add_executable(http-asio ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
target_link_libraries(http-asio ${Boost_LIBRARIES} pthread ssl crypto)