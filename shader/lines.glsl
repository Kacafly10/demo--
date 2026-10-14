// #version 330 core

// // #extension GL_ARB_explicit_attrib_location : require

// layout (location = 0) in vec3 line;

// out vec4 pixl;

// void main() {
    
// }


#version 330 core
layout (location = 0) in vec3 aPos;

void main()
{
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}