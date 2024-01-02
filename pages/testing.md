# :ticket: dipl. Informatiker/in HF Cloud-native Engineer | HF-2.nd-Semester

> Go [back](/pages/implementation.md)
>
> Go [further](/pages/sources.md)

![Banner](/img/banner_testing.png)

# :exclamation: Testing

## Mandatory Use cases

<details><summary>SQS, Lambda fetching data and process it (create instances)</summary>

### Is my Lambda function able to fetch data from SQS?

- [ ] NO

- [x] YES

![CloudWatch](/img/testing/cloudwatch_some_entry.png)
*Figure 14*

<br>

### Does my Lambda function process the given data?

- [ ] NO

- [x] YES

![CloudWatch](/img/testing/cloudwatch_usecase_successfully.png)
*Figure 15*

<br>

### Is the EC2 instance running?

- [ ] NO

- [x] YES

![EC2](/img/testing/ec2_usecase_created.png)
*Figure 16*

![EC2](/img/testing/ec2_usecase_running.png)
*Figure 17*

<br>

### Has the EC2 instance a security group?

- [ ] NO

- [x] YES

![EC2](/img/testing/ec2_security.png)
*Figure 18*

<br>

### Is the EC2 instance public available?

- [ ] NO

- [x] YES

![EC2](/img/testing/ec2_public_web.png)
*Figure 19*

</details>

<details><summary>Lambda other states handling</summary>

### Is my Lambda function to handle different "state" status of [present, deleted, stopped, restarted, start]

- [ ] NO

- [x] YES

<br>

#### Deleted
![EC2](/img/testing/ec2_terminated.png)
*Figure 20*

![EC2](/img/testing/ec2_terminated_2.png)
*Figure 21*

<br>

#### Stopped
![EC2](/img/testing/ec2_stopped.png)
*Figure 22*

![EC2](/img/testing/ec2_stopped_2.png)
*Figure 23*

<br>

#### Restarted
![EC2](/img/testing/ec2_restarted.png)
*Figure 24*

<br>

#### Start
![EC2](/img/testing/ec2_start.png)
*Figure 25*

![EC2](/img/testing/ec2_start_2.png)
*Figure 26*

</details>

<details><summary>Give feedback back to Camunda</summary>

### Can I give a feedback to Camunda to continue the BPM process?

- [ ] NO

- [x] YES

Check [here](/docs/pyzeebe.py) the needed Python script

![Pyzeebe](/img/testing/pyzeebe.png)
*Figure 27*

</details>

<br>

## Test Results Summary

All use cases were successfully executed and marked as complete during testing. This confirms that the scripts meets the specified requirements and functions as intended. The positive results demonstrate the effectiveness of the development and testing teams. Ongoing monitoring and testing in real-world scenarios will ensure continued reliability.

> Jump [up](#🎫-dipl-informatikerin-hf-cloud-native-engineer--hf-2nd-semester)