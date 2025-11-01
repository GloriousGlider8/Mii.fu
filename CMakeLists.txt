cmake_minimum_required(VERSION 3.14)
project(miifu
	VERSION 0.0.2
	DESCRIPTION "Core Mii Implementation"
	LANGUAGES CXX
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

target_compile_features(miifu PRIVATE cxx_std_20)
