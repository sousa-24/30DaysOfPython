#Exercises: Day 5
#1
empty_list=[]

#2
cars=["Ford","Volvo","BMW","Mercedes","Jaguar","Kia","Hyundai"]

#3
print(len(cars))

#4
print(cars[0])
print(cars[3])
print(cars[-1])

#5
mixed_data_types=["Diogo",28,1.65,"Married","Portugal"]

#6
it_companies=["Facebook","Google","Microsof","Apple","IBM","Oracle","Amazon"]

#7
print(it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

#10
it_companies[0]= "Kingston"
print(it_companies)

#11
it_companies.append("Samsung")

#12
it_companies.insert(4,"Huawei")

#13
it_companies[0].upper
print(it_companies)

#14
it_companies_joined = " # ".join(it_companies)
print(it_companies_joined)

#15
print("Facebook" in it_companies)

#16
it_companies.sort()

#17
it_companies.reverse()
print(it_companies)

#18
print(it_companies[0:3])

#19
print(it_companies[-3:])

#20
middle_it_company=it_companies[len(it_companies)//2]
print(middle_it_company)

#21
first_item, *rest=it_companies
it_companies.remove(first_item)
print(it_companies)

#22
it_companies.pop(len(it_companies)//2)
print(it_companies)

#23
it_companies.pop()

#24
it_companies.clear()

#25
del it_companies

#26
front_end=["HTML","CSS","JS","React","Redux"]
back_end=["Node","Express","MongoDB"]
full_stack=front_end+back_end
print(full_stack)

#27
full_stack.insert(full_stack.index("Redux")+1,"Python")
full_stack.insert(full_stack.index("Redux")+2,"SQL")
print(full_stack)

#**********************
# Level 2

#1
ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)
min_age=ages[0]
max_age=ages[-1]
print("Min age:",min_age)
print("Max age:",max_age)
ages.insert(0,min_age)
ages.insert(-1,max_age)
print(ages[len(ages)//2])
average_age=sum(ages)/len(ages)
print("Average:",average_age)
range=max_age-min_age
print("Range:",range)
print(abs(range))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

print(countries[len(countries)//2:len(countries)//2+1])

if len(countries)%2==0:
  list1=countries[:len(countries)//2]
  list2=countries[len(countries)//2:]
else:
    list1=countries[:len(countries)//2+1]
    list2=countries[len(countries)//2+1:]

countries_list=["China","Russia","USA","Finland","Sweden","Norway","Denmark"]

first_country,second_country,third_country,*scandic_countries=countries_list
print("First three countries:",first_country,second_country,third_country,sep=", ")
print("Scandic countries:",scandic_countries)