FROM mongo:7.0.9


# set mongo env
ENV MONGO_INITDB_ROOT_USERNAME=${MONGO_USER}
ENV MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASSWORD}
ENV MONGO_INITDB_DATABASE=${MONGO_DB}

# copy datafiles to home directory
COPY ./init.d/data/texts.json /home/texts.json
COPY ./init.d/data/adjectives.json /home/adjectives.json
RUN chmod 644 /home/*
# copy initial scripts and datafiles in his directory
COPY ./init.d/*.js /docker-entrypoint-initdb.d/
COPY ./init.d/*.sh /docker-entrypoint-initdb.d/

# declare what port container share
expose ${MONGO_PORT}

# start mongo container
# ENTRYPOINT mongod --port ${MONGO_PORT} --bind_ip_all

#R UN mongoimport --db test --collection docs --file example2.json
# mongoexport --db db1 --collection adjectives --out adjectives.json