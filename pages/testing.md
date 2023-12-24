# :ticket: dipl. Informatiker/in HF Cloud-native Engineer | HF-2.nd-Semester

> Go [back](/pages/implementation.md)
>
> Go [further](/pages/)

![Banner](/img/banner_testing.png)

# :exclamation: Testing

## Mandatory Use cases

<details><summary>SQS, Lambda fetching data and process it (create instances)</summary>

### Is my Lambda function able to fetch data from SQS?

- [ ] NO

- [x] YES

![CloudWatch](/img/testing/cloudwatch_some_entry.png)
*Figure*

<br>

### Does my Lambda function process the given data?

- [ ] NO

- [x] YES

![CloudWatch](/img/testing/cloudwatch_usecase_successfully.png)
*Figure*

<br>

### Is the EC2 instance running?

- [ ] NO

- [x] YES

![EC2](/img/testing/ec2_usecase_created.png)
*Figure*

![EC2](/img/testing/ec2_usecase_running.png)
*Figure*

<br>

### Has the EC2 instance a security group?

- [ ] NO

- [x] YES

![EC2](/img/testing/ec2_security.png)
*Figure*

<br>

### Is the EC2 instance public available?

- [ ] NO

- [x] YES

![EC2](/img/testing/ec2_public_web.png)
*Figure*

</details>

<details><summary>Lambda other states handling</summary>

### Is my Lambda function to handle different "state" status of [present, deleted, stopped, restarted, start]

- [ ] NO

- [x] YES

<br>

#### Deleted
![EC2](/img/testing/ec2_terminated.png)
*Figure*

![EC2](/img/testing/ec2_terminated_2.png)
*Figure*

<br>

#### Stopped
![EC2](/img/testing/ec2_stopped.png)
*Figure*

![EC2](/img/testing/ec2_stopped_2.png)
*Figure*

<br>

#### Restarted
![EC2](/img/testing/ec2_restarted.png)
*Figure*

<br>

#### Start
![EC2](/img/testing/ec2_start.png)
*Figure*

![EC2](/img/testing/ec2_start_2.png)
*Figure*

</details>

<details><summary>Give feedvback back to Camunda</summary>

### Can I give feedback back to Camunda to continue the BPM?

- [ ] NO

- [x] YES

Check [here](/docs/pyzeebe.py) the needed Python script

![Pyzeebe](/img/testing/pyzeebe.png)
*Figure*

</details>

<br>

> Jump [up](#🎫-dipl-informatikerin-hf-cloud-native-engineer--hf-2nd-semester)