include(FetchContent)
FetchContent_Declare(
    glus
    GIT_REPOSITORY https://github.com/McNopper/GLUS.git
    GIT_TAG        main
)
FetchContent_MakeAvailable(glus)

target_link_libraries(your_target PRIVATE GLUS)