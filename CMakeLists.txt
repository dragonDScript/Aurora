cmake_minimum_required(VERSION 3.10)

# your project name
project("aurora")

# find includes in the corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# run moc automatically
set(CMAKE_AUTOMOC ON)
# if you're using Widgets and editing .ui forms in Designer
# set(CMAKE_AUTOUIC ON)

message("Looking for Qt...")
# Qt modules (https://doc.qt.io/qt-6/qtmodules.html) you're using in your application
find_package(Qt6 REQUIRED Widgets)
if (${Qt6_FOUND})
    message("Found Qt " ${Qt6_VERSION})
else()
    message("Couldn't find Qt")
endif()

# your source files
set(sources
    main.cpp
)
# name of the .exe file, window flag and the list of things to compile
add_executable(${CMAKE_PROJECT_NAME} WIN32 ${sources})

# also tell CMake to link with the libraries from the line 14
# otherwise it'll think that you wanted to find those just for fun and won't link them
target_link_libraries(
    ${CMAKE_PROJECT_NAME}
    Qt6::Widgets
    )