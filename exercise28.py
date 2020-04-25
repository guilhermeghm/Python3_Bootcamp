##MYy solution
# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

total_donations = 0
# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
for v in donations.values():
    total_donations = total_donations + v

print(total_donations)


##Offical solution
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0

for donation in donations.values():
 total_donations += donation

#Advanced Version 1
total_donations = sum(donation for donation in donations.values())

#Advanced Version 2
total_donations = sum(donations.values())
