# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /cygdrive/c/Users/Asus/AppData/Local/JetBrains/CLion2020.3/cygwin_cmake/bin/cmake.exe

# The command to remove a file.
RM = /cygdrive/c/Users/Asus/AppData/Local/JetBrains/CLion2020.3/cygwin_cmake/bin/cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Lab8.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Lab8.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Lab8.dir/flags.make

CMakeFiles/Lab8.dir/main.c.o: CMakeFiles/Lab8.dir/flags.make
CMakeFiles/Lab8.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Lab8.dir/main.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Lab8.dir/main.c.o   -c "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/main.c"

CMakeFiles/Lab8.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Lab8.dir/main.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/main.c" > CMakeFiles/Lab8.dir/main.c.i

CMakeFiles/Lab8.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Lab8.dir/main.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/main.c" -o CMakeFiles/Lab8.dir/main.c.s

CMakeFiles/Lab8.dir/lex.yy.c.o: CMakeFiles/Lab8.dir/flags.make
CMakeFiles/Lab8.dir/lex.yy.c.o: ../lex.yy.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/Lab8.dir/lex.yy.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Lab8.dir/lex.yy.c.o   -c "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/lex.yy.c"

CMakeFiles/Lab8.dir/lex.yy.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Lab8.dir/lex.yy.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/lex.yy.c" > CMakeFiles/Lab8.dir/lex.yy.c.i

CMakeFiles/Lab8.dir/lex.yy.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Lab8.dir/lex.yy.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/lex.yy.c" -o CMakeFiles/Lab8.dir/lex.yy.c.s

CMakeFiles/Lab8.dir/y.tab.c.o: CMakeFiles/Lab8.dir/flags.make
CMakeFiles/Lab8.dir/y.tab.c.o: ../y.tab.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/Lab8.dir/y.tab.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Lab8.dir/y.tab.c.o   -c "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/y.tab.c"

CMakeFiles/Lab8.dir/y.tab.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Lab8.dir/y.tab.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/y.tab.c" > CMakeFiles/Lab8.dir/y.tab.c.i

CMakeFiles/Lab8.dir/y.tab.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Lab8.dir/y.tab.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/y.tab.c" -o CMakeFiles/Lab8.dir/y.tab.c.s

# Object files for target Lab8
Lab8_OBJECTS = \
"CMakeFiles/Lab8.dir/main.c.o" \
"CMakeFiles/Lab8.dir/lex.yy.c.o" \
"CMakeFiles/Lab8.dir/y.tab.c.o"

# External object files for target Lab8
Lab8_EXTERNAL_OBJECTS =

Lab8.exe: CMakeFiles/Lab8.dir/main.c.o
Lab8.exe: CMakeFiles/Lab8.dir/lex.yy.c.o
Lab8.exe: CMakeFiles/Lab8.dir/y.tab.c.o
Lab8.exe: CMakeFiles/Lab8.dir/build.make
Lab8.exe: CMakeFiles/Lab8.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_4) "Linking C executable Lab8.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Lab8.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Lab8.dir/build: Lab8.exe

.PHONY : CMakeFiles/Lab8.dir/build

CMakeFiles/Lab8.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Lab8.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Lab8.dir/clean

CMakeFiles/Lab8.dir/depend:
	cd "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8" "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8" "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug" "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug" "/cygdrive/d/Formal Languages/BigProject/LFTC/Lab8/cmake-build-debug/CMakeFiles/Lab8.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Lab8.dir/depend

