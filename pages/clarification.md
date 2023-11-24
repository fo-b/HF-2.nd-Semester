# :ticket: dipl. Informatiker/in HF Cloud-native Engineer | HF-2.nd-Semester

> Go [back](/README.md)
>
> Go [further](/pages/planning.md)

![Banner](/img/banner_clarification.png)

# :grey_exclamation: Client expectations

The client, represented by myself, requires the capability to articulate and implement the dynamic provisioning of an EC2 instance. This process relies on the Lambda function's ability to interpret and respond to data received from the Simple Queue Service (SQS). A robust error-handling mechanism is imperative within the Lambda function to effectively structure incoming data, ensuring seamless processing in accordance with established standards for EC2 instance creation. The Lambda function is tasked with orchestrating the synthesis of information derived from SQS into a coherent blueprint for the deployment of EC2 instances.



<br>

## :pencil: Initial position

Given my proficiency in Python development, I anticipate a seamless implementation of various AWS Lambda functions, which essentially leverage Python as their core programming language. To proceed with deployment, I am seeking guidance on the fundamental structure required by AWS.

<br>

Here are the links I used to gain the missing pieces of knowledge of AWX:
I an getting the missing knowledge and information on here:
-   [AWS Lambda](https://docs.aws.amazon.com/lambda/)
-   [AWS SQS](https://docs.aws.amazon.com/sqs/)

<br>

## :checkered_flag: Feasibility - Now-How-Wow-Matrix

### Evaluate ideas based on feasibility and originality
<i>
"Criteria for the selection of ideas are ultimately subjective and depend on the concrete decision-making situation. However, there are general criteria that often ensure a good pre-selection. The criteria feasibility and originality are very common. In combination, these two criteria are an easy-to-use, helpful tool for sorting ideas into different scoring groups. This becomes very clear when the ideas are visualized using a 2×2 matrix. One axis stands for the degree of feasibility, while the other axis stands for the degree of originality. This results in 4 groups (or "clusters") of ideas:
</i>

<br>

<i>

1. low feasibility, no particular originality
2. high feasibility, no particular originality
3. low feasibility, high originality
4. high feasibility, high originality"
</i>

Cf. Prof. Dr. Marin Zec, [sec. 3](https://kreativitätstechniken.info/ideen-bewerten-und-auswaehlen/ideen-bewerten-die-how-wow-now-matrix/#ideen-bewerten-anhand-machbarkeit-und-originalitaet)

<br>

### The How-Wow-Now matrix groups ideas into 4 quadrants
<i>
"The grouping of ideas based on these 4 combinations shows immediately how to proceed with the corresponding ideas. In practice, corresponding English terms have also been established for this: HOW, WOW and NOW. There is no fourth term because the affected group contains ideas that are discarded.
</i>

<br>

<i>

1. Ideas that are not/barely feasible and not particularly original can probably be discarded with a clear conscience
2. NOW!: Ideas that are very feasible, if not particularly original
3. HOW?: Ideas that are probably not that easy to implement, but very original
4. WOW!: Ideas that are both easy to implement and particularly original"

</i>

Cf. Prof. Dr. Marin Zec, [sec. 4](https://xn--kreativittstechniken-jzb.info/ideen-bewerten-und-auswaehlen/ideen-bewerten-die-how-wow-now-matrix/#die-howwownowmatrix-gruppiert-ideen-in-4-quadranten)

<br>

![Machbarkeitsmatrix](/img/feasibility.png)


### :satisfied: NOW!

Today, if there is a need to have multiple EC2 instances, we would interact manually and create the instances with a high error tolerance. This would be very prone to errors and not effective at all.

### :dizzy_face: HOW?

Instead of creating each instance manually, it would be beautiful to have a simple but effective Lambda function that fetches, handles the information, processes it, and deploys it all at once from SQS. With this idea, we can avoid all the manual interactions and minimize the rate of errors. Besides that, it has a straightforward process that is defined and can be changed at any time.

### :sunglasses: WOW!

To automate anything with a manual interaction is like my passion, especially if I see there is a huge time-saving potential and it is possible to do it. Since AWS has provided very strong and detailed documentation for each service, I can always check these documents.

<br>


## :trophy: Goals

1.   Establish an Amazon Simple Queue Service (SQS) infrastructure to effectively manage and
**handle** incoming messages

2.   Engineer a Lambda function to automate the **provisioning** of Amazon Elastic Compute Cloud
(EC2) instances, enhancing operational efficiency

3.   Design a robust communication interface to facilitate **seamless** integration between the
Camunda workflow automation platform and Amazon SQS, in collaboration with Yves Wetter, ensuring a reliable and scalable workflow orchestration solution

<br>

## :pushpin: Project Method

For my semester work, I am using the Kanban method as the project methodology.

> Jump [up](#🎫-hf-dipl-it--1st-semester)
