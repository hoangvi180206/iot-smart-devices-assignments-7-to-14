# Assignment 08 Report - Learn About Cloud Services

## Objective

The objective of this assignment is to understand the main types of cloud service offerings and explain how they are different. The four common cloud service types are Infrastructure as a Service, Platform as a Service, Serverless, and Software as a Service.

## Infrastructure as a Service (IaaS)

Infrastructure as a Service gives users access to cloud infrastructure such as virtual machines, storage, and networking. The user has more control, but also more responsibility. For example, if a developer creates a virtual machine in the cloud, they need to manage the operating system, updates, runtime, and application deployment.

For IoT developers, IaaS can be useful when a custom server is needed, but it is not always the most efficient option because the developer must manage more system details.

## Platform as a Service (PaaS)

Platform as a Service provides a managed platform for running applications. The cloud provider manages the infrastructure, operating system, and runtime environment. The developer mainly focuses on writing and deploying the application.

For IoT developers, PaaS is useful for dashboards, APIs, databases, and web apps that process or display IoT data.

## Serverless

Serverless allows developers to run small pieces of code without managing servers. The code runs only when triggered by an event, such as an HTTP request, an IoT message, or a timer. The cloud provider manages the scaling and infrastructure.

For IoT developers, serverless is very relevant because IoT systems often react to events. For example, an Azure Function can be triggered when a device sends telemetry to IoT Hub, then it can decide whether to turn on a relay or send an alert.

## Software as a Service (SaaS)

Software as a Service is a complete application delivered through the cloud. Users do not manage infrastructure or application code. They only use the software through a browser or application interface. Examples include Microsoft 365, Google Drive, and cloud-based monitoring platforms.

For IoT developers, SaaS can be useful when using ready-made dashboards, monitoring tools, or data analysis platforms.

## Comparison Table

| Cloud type | What the user manages | Example use in IoT |
|---|---|---|
| IaaS | Virtual machines, OS, runtime, app | Custom IoT server |
| PaaS | Application code and data | Web API or dashboard |
| Serverless | Function code | React to IoT telemetry |
| SaaS | Only application settings/data | Ready-made IoT dashboard |

## Which Cloud Offerings Are Most Relevant for IoT Developers?

The most relevant cloud offerings for IoT developers are usually PaaS and Serverless. PaaS is useful for building web applications, APIs, and dashboards. Serverless is useful for reacting to IoT events such as sensor readings, device alerts, and command messages. IaaS is useful when full server control is required, but it takes more work to maintain. SaaS is useful when the developer wants a ready-made tool instead of building everything from scratch.

## Conclusion

Cloud services help IoT developers connect devices, process telemetry, store data, and control actuators remotely. Choosing the right cloud service depends on how much control the developer needs and how much infrastructure management they want to avoid.
