Microservices-based web application utilizing several advanced technologies, including Flask (or a similar Python web framework), RabbitMQ (message queue), Redis (caching or key-value store), and Elasticsearch (real-time search and analytics engine).

 It is designed with scalability, fault tolerance, and real-time data processing in mind. The project also uses OAuth for securing API endpoints, allowing interaction with external services.

The entire architecture leverages Docker containers to achieve portability, ensuring that the app and its dependencies can be replicated and deployed consistently across different environments.

The setup consists of three Elasticsearch nodes (es01, es02, es03), which form a distributed cluster. 

The cluster is configured to provide redundancy, resilience, and high availability.
Each node is assigned specific configurations such as cluster.name, node.name, and discovery.seed_hosts to ensure that they can discover each other and work in unison as a cluster.


Complete Workflow of the System=
Here’s how all these components work together in an integrated system:

HTTP Request

Queueing with RabbitMQ

Processing with RabbitMQConsumer

Data Persistence

Search/Logging

Users can query Elasticsearch to retrieve the stored plans or perform advanced searches.

Key Features:
Microservices-Based Architecture:

The project is built using a microservices approach where different services (application server, Redis, RabbitMQ, Elasticsearch) run independently, providing scalability, fault tolerance, and modularity.
Real-Time Asynchronous Message Processing (RabbitMQ):

The application handles real-time tasks using RabbitMQ as a message broker.
Asynchronous processing ensures that tasks such as creating or updating plans are queued and processed in the background, allowing the application to remain responsive to users.
Multithreading for Concurrent Operations:

The RabbitMQ consumer runs in a separate thread, allowing the application to handle HTTP requests concurrently while consuming messages asynchronously from RabbitMQ without blocking the main execution thread.

Dual Data Persistence (Redis + Elasticsearch)

Redis is used as a caching layer for fast data retrieval, enabling quick lookups and temporary storage.

Scalable Search Engine (Elasticsearch Cluster)

OAuth Authentication for Secure API Access

Containerization with Docker

Message-Driven Architecture

Scalable Caching and Fast Data Access (Redis)

High Availability and Fault Tolerance


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
