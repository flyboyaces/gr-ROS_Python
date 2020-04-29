INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ROS_PYTHON ROS_Python)

FIND_PATH(
    ROS_PYTHON_INCLUDE_DIRS
    NAMES ROS_Python/api.h
    HINTS $ENV{ROS_PYTHON_DIR}/include
        ${PC_ROS_PYTHON_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ROS_PYTHON_LIBRARIES
    NAMES gnuradio-ROS_Python
    HINTS $ENV{ROS_PYTHON_DIR}/lib
        ${PC_ROS_PYTHON_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ROS_PYTHON DEFAULT_MSG ROS_PYTHON_LIBRARIES ROS_PYTHON_INCLUDE_DIRS)
MARK_AS_ADVANCED(ROS_PYTHON_LIBRARIES ROS_PYTHON_INCLUDE_DIRS)
