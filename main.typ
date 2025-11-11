#import "./typst/lib.typ": *

#show: project.with(
  title: "A Hands-On Approach to Robotics Education: Line-Following Systems at WSU",
  author: "Shepard Garrett",
  date: "November 9, 2025",
  remove-hpi-logo: false,
)

= Abstract
Computer engineering students at Wright State University currently have limited extracurricular opportunities to engage in hands-on robotics projects. Most student-led or department-supported projects are organized for computer science majors and primarily emphasize software development. Events such as the *ACM Coding Competition* and the *Alumni Associations Hackathon* are designed for computer science students to strengthen their programming and and development skills. The *Piano Staircase* project has recently sparked some attention from computer engineering students by involving microcontrollers and Time-of-Flight sensors. However, Wright State University has been investing in this idea for the last decade. This proposal introduces a new initiative that offers a novel approach to understanding robotics through research and development.

= Objectives
The scope of this project centers on developing a line-following robot as part of a hands-on learning experience in robotics. The robot will be designed to autonomously track a marked path on the ground using sensor feedback and motor control. The project will progress through structured phases, including system design, hardware construction, software programming, and performance testing.

The main objectives of the project are to:

- Introduce students to the principles of feedback control and sensor integration.

- Develop practical skills in embedded programming and hardware interfacing.

- Demonstrate real-time decision-making and motion control in a physical system.



= Project Design / Methodology

== Hardware Design
Students are provided with a kit to build their robot. Students will be able to attend *Robo-Nights* which will walk them through how to develop a specific iteration of the kit. This will provide students with a baseline to go from, no matter where they are in the project.

== Software and Control
*Expand the 'Software and Control' section. Make it more obvious what's expected in terms of coding.*

The microcontrollers of the robots will be programmed by the students. Visual demonstrations will be provided during the *Robo-Nights*. Demonstration code will be provided for students to become familier with serial communication.

== Evaluation Plan
*Expand the 'Evaluation Plan'. Try and give a point breakdown or something.
*
Student's performance will be evaluated based on their ability to design, build, and program a functional line-following robot. Close to the end of the semester, students will be permitted to enter their robot into a competition to compete against other student's robots. The end goal is not to see who is the winner, but for students to analyze the other created robots and their techniques.

= The Line
*Like will the line be black tape on a carpet floor? Paint on a tiled floor? etc*


= Resources

=== Microboards
- Raspberry Pi Pico -> \$7.495 per Unit
- ESP32 -> \$6.66 per Unit
=== IR Sensors
- TCRT5000 -> \$1.00 Per unit
=== Power
- AA Battery and Connector -> \$2.00 Battery and Connector Cost
=== Motors and Driver Card
- L298N module
- TB6612FNG -> \$2.5 Per unit
- DRV8835
=== Wheels

*'Wheels' and 'Body' of the 'Resources' section should be as specific as the rest (you give exact part names/numbers for the others)*
- #link("https://www.amazon.com/Motor-Leads-Gearbox-Shaft-200RPM/dp/B0D8H89XDY?crid=364L5VKIZS8ZG&dib=eyJ2IjoiMSJ9.UFgu_Yvhkyz5wn-_a44fmB79qwwkvxPz8l572O_A5d0ETSMQYHG1wiS6aTiESQi1j420_JIS2T1vS5DGDtkCMLiNzQ88aqfG_bcAv9-r8lEN4KO-V2K75S80pyiEA2klUh--SHFnizSFyhJ8Oe6fPYE89-7GGR27qXftbOtvCWHqSOKuwV2LGFr40XU64LXJJFkg1yUDzhdZ-g54XowJ_4ibG83J_uN99p8-_K2hw5e8mOHg_iShndrJJdvIrL-xhGEVUJjkUdgLd_L45pRE57krXbbXS3gREO30-j_gMgs.cOwf1hd1MxGrS2VT08GZ66b1maq7rROQwldD4_LiDVg&dib_tag=se&keywords=DC+motor+and+wheels&qid=1762817279&sprefix=dc+motor+and+whee%2Caps%2C154&sr=8-1")[
  wheels + motors -> \$2.5 per wheel
]
- #link("https://www.amazon.com/ASHGOOB-Universal-Furniture-Appliances-Polyurethane/dp/B0DHHJRDDV?dib=eyJ2IjoiMSJ9.GH6LlfuUc24KCMt66moQ0dHQ_Os7PwlFy9PyrK5P__8OsnsMH73VBqAp9Ewe4SQ1AtqYsRsmVqxyWXuHxTfkgZVizeOFZUoqYi019vXGxC4seO41JTU8nmd9WeAIbzKJMlfGP4nKly6u9fp3LI-iLYGd6t-xJSmrXHfOTpye4sPOAJLl1FMPTLmW44Mn2hAKCnYbMXkLWJ2bbSI4YCnUKfvj7AVu2as9WWXcBwP_4KQ.st_mY8ynQLDkpPf8RJghowNnFVt9qPeAYko5FeUSVDQ&dib_tag=se&keywords=Rolling+wheel&qid=1762817512&sr=8-1")[ Front Rolling Wheel -> \$ 1.25 per wheel]
=== Body
The body can be 3d printed

== Overall Budget
*Count for overhead*

Roughtly \$450 for 20 Robots.

= Timeline
*Make a nice looking timeline and try and break it down further.*

The event will be divided into *Five Weeks*:

- Week 1: Students decide their parts list / are given the kits. Their is an overview talk.
- Week 2-4: Visual Demonstrastion over an iteration of the robot.
- Week 5: Performance Analysis and Competition.
