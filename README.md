## Oauth Postman setup
https://blog.postman.com/how-to-access-google-apis-using-oauth-in-postman/

## Docker command to create redis container
```
$ docker run -d --name my-redis-stack -p 6379:6379 redis
```

## Docker command to create RabbitMQ image
```
$ docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

## Start Elastic Search and Kibana cluster
```
To start the cluster
$ docker-compose up

To stop the cluster
$ docker-compose down
```

### Contents of .env file
```
# .env
PYTHON_ENV = "development"

DEV_PORT = "5000"
DEV_HOST = "localhost"
REDIS_DEV_HOST = "localhost"
REDIS_DEV_PORT = "6379"
RABBITMQ_DEV_HOST = "localhost"
RABBITMQ_DEV_PORT = "15672"
DEV_VERSION = "v1"
DEV_OAUTH_CLIENT_ID = "<OAUTH_CLIENT_ID>"
DEV_ELASTIC_HOST = "http://localhost:9200/"

PROD_PORT = "5000"
PROD_HOST = "localhost"
REDIS_PROD_HOST = "localhost"
REDIS_PROD_PORT = "6379"
RABBITMQ_PROD_HOST = "localhost"
RABBITMQ_PROD_PORT = "15672"
PROD_VERSION = "v1"
PROD_OAUTH_CLIENT_ID = "<OAUTH_CLIENT_ID>"
PROD_ELASTIC_HOST = "http://localhost:9200/"
```

### Elastic Search Dev Console queries
```
# Get Plan
GET _search
{
  "query": {
    "match": {
      "_id": "12xvxc345ssdsds-508"
    }
  }
}

# Get Plans children
GET _search
{
  "query": {
    "has_parent": {
      "parent_type": "plan",
      "query": {
        "term": {
          "_id": "12xvxc345ssdsds-508"
        }
      }
    }
  }
}

# Get Parent of planCostShare with copay greater than or equal to 1
GET _search
{
  "query": {
    "has_child": {
      "type": "planCostShare",
      "query": {
        "range": {
          "copay": {
            "gte": 1
          }
        }
      }
    }
  }
}

# Get planCostShare of Plan
GET _search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "objectType": {
              "value": "membercostshare"
            }
          }
        },
        {
          "has_parent": {
            "parent_type": "plan",
            "query": {
              "term": {
                "_id": "12xvxc345ssdsds-508"
              }
            }
          }
        }
      ]
    }
  }
}

# Get linkedPlanService of Plan
GET _search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "objectType": {
              "value": "planservice"
            }
          }
        },
        {
          "has_parent": {
            "parent_type": "plan",
            "query": {
              "term": {
                "_id": "12xvxc345ssdsds-508"
              }
            }
          }
        }
      ]
    }
  }
}

# Get linkedPlanServices children
GET _search
{
  "query": {
    "has_parent": {
      "parent_type": "linkedPlanService",
      "query": {
        "term": {
          "_id": "27283xvx9asdff-504"
        }
      }
    }
  }
}

# Get planCostShare of linkedPlanService
GET _search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "objectType": {
              "value": "membercostshare"
            }
          }
        },
        {
          "has_parent": {
            "parent_type": "linkedPlanService",
            "query": {
              "term": {
                "_id": "27283xvx9asdff-504"
              }
            }
          }
        }
      ]
    }
  }
}

# Get linkedService of linkedPlanService
GET _search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "objectType": {
              "value": "service"
            }
          }
        },
        {
          "has_parent": {
            "parent_type": "linkedPlanService",
            "query": {
              "term": {
                "_id": "27283xvx9asdff-504"
              }
            }
          }
        }
      ]
    }
  }
}
```
