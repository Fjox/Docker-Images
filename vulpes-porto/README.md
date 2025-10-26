Vulpes Porto\
Rengyr, <mail@rengyr.eu>

Mastodon (works on GoToSocial and Mitra as well !) bot to post remotely or locally hosted photos daily at set times. The bot will prioritize images that weren't yet posted. In case of exhaustion of new photos the bot will post random photo from the pool.

### Running the bot

The bot takes one mandatory argument (--config, -c) which is the location of the configuration json file. The bot supports optional options:

`--now, -n` that will cause the bot to post one image on start-up and then continue based on the schedule in the configuration json file

`--check, -C` that will check whether configuration file and token is valid and exits after

Example of starting bot:
```
Normal start:
./vulpes_porto --config ./config_example.json

Start with posting one image immediately:
./vulpes_porto --config ./config_example.json --now
```

It is also possible to run vulpes-porto in a docker container via 3rd party docker image ```git.fjox.win/fjox/vulpes-porto:latest```. to configure it mount your config file at ```/app/config.yaml``` in the container.

### Configuration file

Server side configuration example is in config_example.toml (json and yaml format is as well supported). Fields of this configuration file are described inside of the example configuration files.

### Image sources file

Json file with links to images has following structure: list of records where each record has "location" which is a link to the remotely hosted photo or local photo. Each record can have optional message that will get posted with the photo, optional alt text for the photo, and optional content warning.

Using photos from local filesystem requires prefix "file:" in the "location" field in the json. Using local photos as well requires to have setup "local_path" in server side configuration file (see config_example.toml example).

Example of json structure:
```
[
    {
	"msg": "Augsburg Zoo, Germany",
	"location": "https://example.com/sources/IMG_1978.JPG"
    },
    {
	"location": "https://example.com/fennecbot/sources/IMG_1955.JPG"
    },
    {
	"msg": "Augsburg Zoo, Germany",
	"location": "https://example.com/fennecbot/sources/0001.jpg",
	"alt": "Fennec sitting on a sand dune"
    },
	{
	"msg": "Somewhere on field, Germany",
	"location": "https://example.com/fennec/sources/0002.jpg",
	"alt": "Fennec sitting on a grass",
	"content_warning": "Dangerously beautiful fox"
    },
	{
	"msg": "Augsburg Zoo, Germany",
	"location": "file:fox.jpg"
    }
]
```

### Helpful scripts

#### Generate sources json file

Simple script [sources-gen.py](./scripts/sources-gen.py) can be used to generate sources json with _all_ (incl. non image ones) files in the given folder and its subfolders. First and only parameter of the script is folder with the images. Sources json is printed to standard output.

Example usage: `python3 scripts/sources-gen.py ~/bot-photos > sources.json`

<br>

Example of GoToSocial account that is using Vulpes Porto:\
[@toomanyfoxes@icy.arcticfluff.eu](https://icy.arcticfluff.eu/@toomanyfoxes)

Example of Mitra account that is using Vulpes Porto(Docker):\
[@fox@foxes.download](https://foxes.download/@fox)
