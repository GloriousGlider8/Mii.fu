cmake_minimum_required(VERSION 3.14)
project(miifu
	VERSION 0.0.2
	DESCRIPTION "Core Mii Implementation"
	LANGUAGES CXX
)

execute_process(COMMAND_ERROR_IS_FATAL ANY
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
	COMMAND fut -D CPP -n miifu -l cpp src/Readers.fu src/FFLResource.fu -o gen/FFLResource.cpp
	COMMAND fut -D CPP -n miifu -l cpp mii-fusion-experiments/Ver3StoreData/Ver3CharInfo.fu mii-fusion-experiments/Ver3StoreData/Ver3StoreData.fu mii-fusion-experiments/Ver3StoreData/Crc16Ccitt.fu mii-fusion-experiments/Ver3StoreData/Utf16ToUtf8Converter.fu -o gen/Ver3StoreData.cpp
)

option(MIIFU_BUILD_SHARED "Build miifu as a shared library" OFF)

if(MIIFU_BUILD_SHARED)
	add_library(miifu SHARED)
else()
	add_library(miifu STATIC)
endif()

target_sources(miifu PRIVATE
	gen/FFLResource.cpp
	gen/Ver3StoreData.cpp
	gen/FFLResource.hpp
	gen/Ver3StoreData.hpp
)

target_include_directories(miifu
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/gen
)

target_compile_features(miifu PUBLIC cxx_std_20)