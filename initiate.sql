CREATE TABLE IF NOT EXISTS task_node (
    uuid UUID PRIMARY KEY,
    action VARCHAR(255) NOT NULL,
    start TIMESTAMP,
    "end" TIMESTAMP,
    status VARCHAR(50),
    log TEXT
);

CREATE TABLE IF NOT EXISTS time_when ( 
    id serial primary key, 
    granularity varchar(50), 
    timestamp bigint unique, 
    year int, 
    month int, 
    day int,
    hour int
);

CREATE TABLE IF NOT EXISTS project ( 
    id serial primary key, 
    project varchar(100) unique
);

CREATE TABLE IF NOT EXISTS access ( 
    id serial primary key, 
    access varchar(100) unique
);

CREATE TABLE IF NOT EXISTS agent ( 
    id serial primary key, 
    agent varchar(100) unique
);
    
CREATE TABLE IF NOT EXISTS views (
    project_id int references project(id), 
    agent_id int references agent(id), 
    access_id int references access(id), 
    time_id int references time_when(id), 
    views bigint,
    PRIMARY KEY (project_id, agent_id, access_id, time_id)
);