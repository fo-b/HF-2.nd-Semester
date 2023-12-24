# :ticket: dipl. Informatiker/in HF Cloud-native Engineer | HF-2.nd-Semester

> Go [back](/pages/planning.md)
>
> Go [further](/pages/testing.md)

![Banner](/img/banner_implementation.png)

# :exclamation: Implementation

In this segment, I aim to outline each individual step I've taken, highlighting instances where difficulties arose. My objective is to ensure that this portion remains easily understandable for a broad audience and remains reproducible at any given point in time.

## :green_book: Working environment

My current work environment is on AWS, inside the Lambda function, where I developed and tested the main function using manual JSON injections. You can track the entire development status of the Lambda function [here](/docs/lambda_func/). It is primarily built in Python.

## :closed_lock_with_key: Access AWS Academy Learner Lab

To access the lab, I simply log in to the AWS Academy using my TBZ school account information. After logging in, I can easily start the environment with the click of a button:

![AWSLabStart](/img/awslabstart.png)
*Figure 3*

A few minutes later I am able to click on the "AWS" title and it will forward me to the described AWS environment:

![AWSLabRunning](/img/awslabrunning.png)
*Figure 4*

---

### Create Lambda function

Here you can see I have decided to go along with the name "CamundaProcessCreateEC2". As the runtime, I am choosing Python as the main language. Since I am inside the AWS Academy Lab, it is necessary to use the "LabRole" role for the execution; otherwise, the Lambda function is not able to run it successfully:

![AWSLabCreateLambdaFunction](/img/awslabcreatelambdafunction.png)
*Figure 5*

After a few seconds, the previously created function now looks like this:

![AWSLabCreatedLambdaFunction](/img/awslabcreatedlambdafunction.png)
*Figure 6*

---

### Run once the Lambda function

Now we can quickly test if we are able to run our created function:

![AWSLabLambdaFunctionRunning](/img/awslablambdafunctionrunning.png)
*Figure 7*

After running successfully our Lambda function we are now sure, the creation and setup of our function was done correctly

---

### Create SQS Queue

To prevent our Lambda function from triggering manually each time, I can easily create an SQS Queue:

 ![AWSSQSCreateQueue](/img/awssqscreatequeue.png)
 *Figure 8*

---

### Add the Trigger in Lambda function

Easily we can now choose our SQS queue from dropdown:

![AWSLambdaFunctionAddSQS](/img/awslambdafunctionaddsqs.png)
*Figure 9*

Now there we need to wait a few minutes until the Trigger state changes to "Enabled"

![AWSLambdaFunctionAddSQS](/img/awslambdafunctionaddsqsenabled.png)
*Figure 10*

---

### Run once SQS injection

Now we can easily test if the SQS Trigger inside of our Lambda function will run or not. For that we can send messages manually like this:


![AWSSQSMessageTest](/img/awssqsmessagetest.png)
*Figure 11*

![AWSSQSMessageTestResponse](/img/awssqsmessagetestresponse.png)
*Figure 12*

![AWSSQSMessageTestLog](/img/awssqsmessagetestlog.png)
*Figure 13*

With these provided screenshots, it is securely proven that the SQS Trigger fetches the data and processes it correctly.

---

## Develop the Lambda function

[Here](/docs/lambda_func/), you can see the development and improvement of the Lambda function, which I strive to perfect almost every day.

> Jump [up](#🎫-dipl-informatikerin-hf-cloud-native-engineer--hf-2nd-semester)