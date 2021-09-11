<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- ABOUT THE PROJECT -->
## About The Project

This file converter is a quick way to read in varibles from .cf files (netCDF) and convert to CSV. It was initially created to process large amounts of Physical Oceanography data to be consumed and joined in an easy way.

If you're wishing to test this with Chlorophyll, dowload data from here:
https://oceancolor.gsfc.nasa.gov/l3/

Add the downloaded files to the folders mentioned in script.py & update the variable names if needed.


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Packages

The below are packages required for this project 
* netCDF4                        
* xarray                                    
* os
* numpy
* matplotlib

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install packages as mentioned above
   ```sh
   pip3 install <package>
   ```

### Data
The below link will take you to EarthData which is a NASA initiative for Ocean Colour. You will need to create an account to download the data.

https://oceancolor.gsfc.nasa.gov/l3/

<!-- USAGE EXAMPLES -->
## Usage

This file converter can be useful when working with large amount of satellite data or any type of .nc file data. It helps to convert to csv, however depending on the conversion required it will need further tweaking.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
