#import "./typst/lib.typ": *

#show: project.with(
  title: "A Hands-On Approach to Robotics Education: Line-Following Systems at WSU",
  author: "Shepard Garrett",
  date: "November 9, 2025",
  remove-hpi-logo: false,
)
= Abstract
This project proposes the development of a line-following robot program at Wright State University as a means to enhance hands-on learning within the field of computer engineering. Students will learn to program embedded systems, process sensor data, and develop a functional system. Through workshops and *_Robo-Night_* sessions, students will design, build, and program autonomous robots capable of following a marked path using infrared sensors and real-time feedback control.
\
This initiative aims to strengthen the university's commitment to experiential learning. It will support academic growth and enhance Wright State University's public image as a hub for applied robotics education.

= Introduction
Computer engineering students at Wright State University currently have limited extracurricular opportunities to engage in hands-on robotics projects. Most student-led or department-supported projects are organized for computer science majors and primarily emphasize software development. Events such as the *_ACM Coding Competition_* and the *_Alumni Associations Hackathon_* are designed for computer science students to strengthen their programming and development skills. The *_Piano Staircase_* project has recently sparked some attention from computer engineering students by involving microcontrollers and Time-of-Flight sensors. However, Wright State University has been investing in this idea for the last decade. This proposal introduces a new initiative that offers a novel approach to understanding robotics through research and development.

= Objectives
The scope of this project centers on developing a line-following robot as part of a hands-on learning experience in robotics. The robot will be designed to autonomously track a marked path on the ground using sensor feedback and motor control. The project will progress through structured phases, including system design, hardware construction, software programming, and performance testing.

The main objectives of the project are to:

- Introduce students to the principles of feedback control and sensor integration.

- Develop practical skills in embedded programming and hardware interfacing.

- Demonstrate real-time decision-making and motion control in a physical system.



= Project Design / Methodology

== Hardware Design
Students are provided with a kit to build their robot. Students will be able to attend *_Robo-Nights_* which will walk them through how to develop a specific iteration of the kit. This will provide students with a baseline to build from, no matter where they are in the project.

== Software and Control
The microcontrollers of the robots will be programmed by the students. Visual demonstrations will be provided during the *_Robo-Nights_*. Demonstration code will be provided for students to become familiar with serial communication. Students will be expected to code:
- IR sensing and data collection (Vision)
- Motors (Movement)
- Communication with the microcontroller and external devices (Connecting Vision with Movement)

== Evaluation Plan
Students performance will be evaluated based on their ability to design, build, and program a functional line-following robot. Close to the end of the semester, students will be permitted to enter their robot into a competition to compete against other student's robots. The end goal is not to see who is the winner, but for students to analyze the other created robots and their techniques. The competition will be evaluated based on:
- Robot correctly following line
- The speed of the robot and it's control 

= The Line
The Line will be black duct tape on a white ground.
- 1.88 in

= Resources

=== Microboards
- #link("https://www.amazon.com/Raspberry-Pi-Pico-Development-Integrated/dp/B0BDLHMQ9C?crid=2QWLD0HO8I8XA&dib=eyJ2IjoiMSJ9.UgC9ruITkp0J6Jz3B674QeD_5s_2kVFK-6pw5wXpUodfElFRplaSQOZhTe1eyJGW_NZ-qxbTOIfu35IV2mydkFNfFNZVSDUud4krLx1GYXQS74naLyVAk1EY4jbEn_y4arPsF6ZJr8_HYMuSZiTgT3COMBbr8ceVned1HU4e-vKzxk7-d4xzRGgnnNwmYV-wbD4byN7s60i4BfqUweYAeJvjLf1jbBLrnrm35iB2NKU.gvOF2_EkX2iEsAlGF84ou5yUkFpKhhfYhDO18PydTzU&dib_tag=se&keywords=Raspberry+Pi+Pico&qid=1767758016&sprefix=tcrt5000%2Caps%2C172&sr=8-2")[Raspberry Pi Pico -> \$7.495 per Unit]
=== IR Sensors
- #link("https://www.amazon.com/HiLetgo-Channel-Tracing-Sensor-Detection/dp/B00LZV1V10?crid=1AVL4WKF6UNV4&dib=eyJ2IjoiMSJ9.3EaZdxvNlScNahkByoJoKScqiQ5ZotuDmqIfqgRcuOHmMFXGhZs8lJhVdgAryfAVmHzJE-uV9yEmI1VnEZOTerQE2T38YcpFEYQ8Y-Lupbr4h_FXGerpxel8ek8ZJtIEVZcyvARQ-3RXWaIX6MoRJsQKmhKyqesRgrhZgr5KJHJY50Jgw1PeOjDuS8emgtIpFSTzEPC-ajW5VHpV09Hfiu_EPHKWp-LkEKHhu4E1IQU.6sWQbwM4RJNEjmccJ0jj0HimMF6KXYfOrDDTMgsCCQo&dib_tag=se&keywords=TCRT5000&qid=1767757994&sprefix=4+battery+holder%2Caps%2C215&sr=8-4")[TCRT5000 -> \$1.00 Per unit]
=== Power
- AA Battery and Connector -> \$2.00 Battery and Connector Cost
- #link("https://www.amazon.com/WAYLLSHINE-2Pcs-Battery-Holder-Leads/dp/B09V7Z4MT7?crid=1EQIY8Z00YCSL&dib=eyJ2IjoiMSJ9.aWNVgKH8jF-fjeQsJ2eIoEshpvBH6iaTRzpxByE539AITBXsZKATAprsQ_CjKTZgwtah6cgMDHyoRZ1entsILHBwVLTrA3JRrebZkt3sfOWhvbQNdN5BfnNZrg9hBNywnTfaDR_3QEvmf0sbfhTLygfLIiFPaCAfwaBHfqy4Hfmx4R2XmHx7O5MSR1me5kvj0HDXsC_TA24OFKpLFTHooP2n7EOxzJt5DZC9-90X0Mw.vyxVNtT7sb2GDQe7bN0HtwecXv6t9k4rOnyTHbU1j34&dib_tag=se&keywords=2+battery+holder&qid=1767757891&sprefix=2+battery+holder%2Caps%2C169&sr=8-3")[2 AA holder]

- #link("https://www.amazon.com/VWEICYY-Battery-Holder-housing-Without/dp/B0DZX39MHK?crid=3LDP5FNOCINJJ&dib=eyJ2IjoiMSJ9.hQVCzDNE3wFs2GVL11to1kfnn5_5dWcSh48T1yZtDPQE7G59I1a7JqrO_JIYD79xBst5sb6zjju136MHaqKgAYKSu6ImIVALDyv1MUIVKiGh0aq6p51b-ALEnRXef2vn2HPBr4lGMttat714J74pDu6CkLcHz6iyFWBiWh1jwgxPyq1dwr4DkaCohCO8R10Eplqv82v053zliTxhEGYPEkHpMH5zKbv449I2Qeqvqz0.0pj7VFFmkaFhwaZy_UJjOno9h9O_nOHNlEIDwgnzVjQ&dib_tag=se&keywords=4+battery+holder&qid=1767757938&sprefix=battery+holder%2Caps%2C225&sr=8-3")[4 AA holder]
=== Motors and Driver Card
- #link("https://www.amazon.com/Dual-Motor-Driver-Module-TB6612FNG/dp/B08J3S6G2N?dib=eyJ2IjoiMSJ9.0k2ayQl-KVuMhVoPU5a0jykgUcFeQfu3gZWPti-HI_3e2-ZhugFhzHJDPFmm7VuuplwgH-svAkH1EUbOU0rraD0az8aBqPXuCB7r7pe4bY2X1F3h5wvcqh-wF880jswmQ_piFW1gTMjE_LwMAVM2fT9KUuS1_a0TLsr7xsCfcJkwgZ1dXWCrCM0QtDZ4k9XxlDINeCWVw2CcVMM-XxzNKKXkZGirlDSEdOTYPA9vNWc.WyCg_lip2tp4vzqkbj_6JHBRRxwOLuWfxV_MoUN5Srg&dib_tag=se&keywords=tb6612fng&qid=1767757810&sr=8-4")[TB6612FNG -> \$2.5 Per unit]
=== Wheels
- #link("https://www.amazon.com/Motor-Leads-Gearbox-Shaft-200RPM/dp/B0D8H89XDY?crid=364L5VKIZS8ZG&dib=eyJ2IjoiMSJ9.UFgu_Yvhkyz5wn-_a44fmB79qwwkvxPz8l572O_A5d0ETSMQYHG1wiS6aTiESQi1j420_JIS2T1vS5DGDtkCMLiNzQ88aqfG_bcAv9-r8lEN4KO-V2K75S80pyiEA2klUh--SHFnizSFyhJ8Oe6fPYE89-7GGR27qXftbOtvCWHqSOKuwV2LGFr40XU64LXJJFkg1yUDzhdZ-g54XowJ_4ibG83J_uN99p8-_K2hw5e8mOHg_iShndrJJdvIrL-xhGEVUJjkUdgLd_L45pRE57krXbbXS3gREO30-j_gMgs.cOwf1hd1MxGrS2VT08GZ66b1maq7rROQwldD4_LiDVg&dib_tag=se&keywords=DC+motor+and+wheels&qid=1762817279&sprefix=dc+motor+and+whee%2Caps%2C154&sr=8-1")[
  wheels + 6V 1:48 TT DC gearbox motors -> \$2.5 per wheel
]
=== Body
Bring your own carboard box.

=== Screws
6 M?, don't know length.
1 Acorn Cap, don't know size or length

== Overall Budget
Roughly \$450 for 20 Robots.
- Cost does not include parts being broken or not working

= Timeline
The event will be divided into *_Five Weeks_*:

== Week 1: Students are given the kits. 
Students will be provided with kits and an introduction. The talk will go over the logistics of the event. Students are encouraged to participate in the *_Labs_* as much as possible.
== Week 2-4: Visual Demonstrations and Robo-Nights
=== Week 2
Week 2 will cover the motors and the raspberry pi pico. Students are expected to have their robots at least moving in a straight line by the end of this week.
=== Week 3
Week 3 will cover the vision of the robot. There will be a live demonstration explaining how to process data from IR sensors. Students will be expected to have their robots moving in the direction of the tape.
=== Week 4
Week 4 will focus on optimizations. Students will learn how to bridge gaps in the lines with their robots. Different style choices in how the robot reacts to *_weird_* lines will be discussed.
== Week 5: Performance Analysis and Competition.
The competition will be held on this week. Students will bring their robots and compete, if they wish, against the other robots.
