# Transformer: Weather DAT File Parser

Loads Weather DAT file contents to GeoStreams database.

### Sample Docker Command Line

Below is a sample command line that shows how the Weather DAT File Parser Docker image could be run.
An explanation of the command line options used follows.
Be sure to read up on the [docker run](https://docs.docker.com/engine/reference/run/) command line for more information.

The files used in this sample command line can be found on [Google Drive](https://drive.google.com/file/d/1St8vvAqnYR4nndXjahFi8hF4U4CBYvGc/view?usp=sharing).

```sh
docker run --rm --mount "src=/home/test,target=/mnt,type=bind" agpipeline/weather_datparser:3.0 --working_space "/mnt" --clowder_url "<Clowder URL>" --clowder_key "<Clowder Key>" "/mnt/2017-05-08"
```

This example command line assumes the source files are located in the `/home/test` folder of the local machine.
The name of the image to run is `agpipeline/weather_datparser:3.0`.

We are using the same folder for the source files and the output files.
By using multiple `--mount` options, the source and output files can be separated.

**Docker commands** \
Everything between 'docker' and the name of the Docker image are docker commands.

- `run` indicates we want to run an image
- `--rm` automatically delete the image instance after it's run
- `--mount "src=/home/test,target=/mnt,type=bind"` mounts the `/home/test` folder to the `/mnt` folder of the running image

We mount the `/home/test` folder to the running image to make files available to the software in the image.

**Image's commands** \
The command line parameters after the image name are passed to the software inside the image.
Note that the paths provided are relative to the running image (see the --mount option specified above).

- `--working_space "/mnt"` specifies the folder to use as a workspace
- `--clowder_url "<Clowder URL>"` the URL of the Clowder instance to load weather data to
- `--clowder_key "<Clowder Key>"` the key associated with the Clowder account to use at the specified Clowder URL
- `"/mnt/2017-05-08"` is the name of the folder to look at for Weather DAT files. A combination of files and folders can be specified.

It's also possible to specify the Clowder URL and key by setting the `CLOWDER_URL` and `CLOWDER_DEFAULT_KEY` environment variables.
