cmake_minimum_required(VERSION 3.9)

set(CMAKE_EXPORT_COMPILE_COMMANDS 1)

FIND_PACKAGE(OpenSSL)

if (OPENSSL_FOUND)
    INCLUDE_DIRECTORIES(${OPENSSL_INCLUDE_DIR})
else()
    MESSAGE(FATAL_ERROR "Could not find OpenSSL.")
endif ()

FIND_PACKAGE(CURL)

if (CURL_FOUND)
    INCLUDE_DIRECTORIES(${CURL_INCLUDE_DIR})
else()
    MESSAGE(FATAL_ERROR "Could not find Curl.")
endif ()

add_executable(http-curl ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
target_link_libraries(http-curl ${CURL_LIBRARIES} pthread ssl crypto curl)
