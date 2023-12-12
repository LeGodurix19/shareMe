
# ShareME

![](https://img.shields.io/badge/Langage-Python-green.svg) ![](https://img.shields.io/badge/Framework-Django-grey.svg) ![](https://img.shields.io/badge/Project_type-Personnal-red.svg)

ShareME is a link-sharing platform.

All you have to do is create an account and provide your links, then you can share your personal page with the url you want!

## Deployment

To deploy the project, you need to install docker.

```bash
git clone ...
```

Once the repo is on your computer, use the .env_example file to create the .env file.

```bash
docker-compose build && docker-compose up -d
```

Once this has been done, you can connect to the [site](http://127.0.0.1:8000/)!

Empty links?  No problem, go to the [database](http://127.0.0.1:8000/admin/) to add some!

PS: To add a link, you need a Link in the db you want to link to.


## Authors

- [@Goudurix](https://www.github.com/goudurix)