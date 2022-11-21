# Processing an API Response

import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()

# Process results
print(response_dict.keys())

# We import the requests module.
# We store the URL of the API
# We define headers for the API call that ask explicitly to use this version of the API. 
# Then we use requests to make the call to the API.
# We call get() and pass it the URL and the header that we defined and we assign the response object to the variable R
# The response object has an attribute called status_code, which tells us whether the request was successful
# The api return information in JSON format  so we use the json() method to convert the information to a Python Dict.


# Working with the Response Dictionary

# Processing an API Response

import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")


# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
    

# We print the value associated with 'total_count', which represents the total number of Python repositories on GitHub
# The value associated with 'items' is a list containing a number of dictionaries,
# Each of which contains data about an individual Python repository.
# We store the the list of dictionaries in repo_dicts we then print the length of repo_dicts
# We pull out the first item from repo_dicts and store it in repo_dicts
# We then print out the number of Keys in the dictionary to see how much information we have.




# We pull out the values for some keys in the repo_dict

import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")


# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict ['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

# Here we print the values for a number of keys from the first repository dictionary.



# Summarizing the Top Repositories
# When we make a visualization for this data, we'll want to include more than one repository. 
# Lets write a loop to print selected information about each repository the API call returns so we can include them in a visualization:

import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")


# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")


print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Description: {repo_dict['description']}")

# We print an introfuctory message at & we loop through all the dictionaries in repo_dicts.
# Here we loop through Name of Project, Owner, Stars & URL



# Monitoring API Rate Limits
# Most API's are rate limited, which means there's a limit to how many requests you can make in a certain amount of time.
# To see if you're approaching GitHub's limits.





# Visualizing Repositories Using Plotly