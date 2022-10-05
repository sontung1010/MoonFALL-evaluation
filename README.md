# Incoming Software Engineer Evaluation

In this repo are a series of coding questions and three quick programming exercises to evaluate where to best place you. Pull this repo and change the upstream branch from the MoonFall one to a personal public repository. A guide on how to do that can be found [here](https://devconnected.com/how-to-change-git-remote-origin/). Please fill out the info section on this page, the complete the quick answer questions below. 

There are also 3 programming challenges written in python 3. If you do not know python you can answer in detailed pseudocode or c++. Detailed descriptions for the tasks are in their folders README files. 

 - [C1: Game of Life](C1/README.md)
 - [C2: Matrix Operations](C2/README.md)
 - [C3: Calculator](C3/README.md)

When you are finished, push the code to your own repo and send the link to maxwildersmith@gmail.com.

---
## Info

Name: Tung Do

Email: tungdo@cpp.edu

Project you are applying for: MoonFALL


---
## Quick Answer Questions
For the following questions answer as best you can, if you do not know, either make your best guess or skip the question. These questions are designed to cover all the potential roles for a project so it is not expected to know the answer to all of them. For the short answer ones answer is one or two sentences.

Sample:

Which of these is the number 5?
 - 1
 - 0
> - 5
 - 4

What is one difference between a float and an int?

> An int is a whole integer number while a float can be a decimal value.

### Questions:
---

**General**

What does an activity diagram show?
> They show the flow between the actions in an activity.

Which of these languages offers the lowest level of control and fastest execution?
 - Python
 - C#
 - Java
> - C


What is the purpose of version control systems (VCS) such as Git or Mercurial?
> tracks changes to a file or set of files over time so that you can recall specific versions later
---
**Embedded Systems**

Which level of cache would be accessible by only a single core on a multi-core chip?
> - L1
 - L2
 - L3
 - All levels


Explain one difference between any of these 2 protocols: I2C, SPI, UART:


What is a feature Java has that C++ does not?
 - Object oriented classes
 - Lambda expressions
 - Data streams
> - Implicit garbage collection


Name one major concern when developing for embedded systems and edge computing such as a deployed Jetson or Raspberry Pi:


Which of the following is a job for the DHCP server?
 - Route packets out to the internet
 - Make particular ports available for access on the inter/intranet
> - Assign IP addresses on the network
 - Look up what domain name maps to an address on the internet

---
**Linux**

What does the permission code 777 represent (as used in `chmod 777`)?
> all can read/write/execute (full access)

Which of these commands sets and environment variable in Linux?
 - export VAR=val
 - export $VAR=val
 - echo VAR=val
> - echo $VAR=val


What is one major role of systemd?
> systemd provides a logging daemon and other tools and utilities to help with common system administration tasks

---
**AI**

Which of these network architectures would be best suited for processing text?
 - Convolution Neural Network
> - Recurrent Neural Network
 - Multilayer Perceptron
 - U-Net


What is one solution to the vanishing gradient problem in backprop?
> use other activation funtions

What is the traditional flow of interactions for a reinforcement learning agent?
 - Read the current state, take an action, environment updates state
 - Make a prediction, evaluate the loss from a target, update model with backprop
> - Generate result, compare result to similar objects of the class, improve discriminator and predictor


Briefly describe either branch and bound or dynamic programming:
> Branch and bound: the set of candidate solutions is thought of as forming a rooted tree with the full set at the root

What is the main challenge with implementing A*:
 - Picking the correct heuristic
 - Initialization parameters
> - Solution will not converge
 - Too long of an execution compared to other common pathfinders
