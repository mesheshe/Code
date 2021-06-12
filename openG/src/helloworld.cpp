#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <header/main.h>
#include <iostream>

const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

int main()
{
    // initializes the open gl 
    glfwInit();
    // Specify the version of openGL
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    // Choose whether to use backward compatible verses moderm version 
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    
    // Creates the window, first two argument specifies the width and height respectively
    // 3rd argument specifes the name of window, 4th argument windowed or fullscreen
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGl",NULL,NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    // After creating the window, open it.
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to intitialize GLAD" << std::endl;
        return -1;
    }
    
    // draw the window at least once since draw is inside a function call 
    // that will only run when pollEvents says there has been a resize in window
    draw(window);

    while (!glfwWindowShouldClose(window))
    {
        processInput(window);
        glfwPollEvents();
    }

    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;
}

// changes the screen size
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0,0, width, height);
    draw(window);
}

// Process keyboard input, hit ESC key to exit
void processInput(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}

void draw(GLFWwindow* window)
{
    glClearColor(0.2f,0.3f,0.3f,1.0f);
    glClear(GL_COLOR_BUFFER_BIT);    
    glfwSwapBuffers(window);
        
}