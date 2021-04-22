# Knight Hacks 2021 Backend

Backend server for Knight Hacks '21

## Contents

- [QuickStart](#quickstart)
- [Backend Environment Variables](#backend-environment-variables)
- [Testing](#testing)
- [WebSockets](#websockets)


## QuickStart

**Requirements:**

- MongoDB Server
- Python 3.9

1. Install the requirements.

`pip install -r requirements.txt`

2. Run the server

`python -m src run --port=5000`


## Backend Environment Variables

These are the default values, feel free to change them.

```
APP_SETTINGS=src.config.ProductionConfig
MONGO_URI=mongo://localhost:27017/test
```


## Testing

1. Install the dev requirements.

`pip install -r requirements-dev.txt`

2. Run the tests

`python -m src test`


# Websockets

## Live Updates

Namespace
: `/live_updates`

When you connect to this namespace, you will immediately be sent the **hello** event.

The **hello** event sends a json message containing a list of all the LiveUpdates currently in the database.

A LiveUpdate object will look like

```json
{
  "ID": number,
  "message": "string",
  "timestamp": "iso8601 date-time"
}
```

You can request the entire list of LiveUpdates from the server by sending a **reload** event, which will cause the server to send back a **reload** event which will contain the same message as the **hello** event.


### Subscribed Events

#### NewLiveUpdate

This event is called when there is a new LiveUpdate, which sends a json message containing a LiveUpdate object.

```json
{
  "ID": number,
  "message": "string",
  "timestamp": "iso8601 date-time"
}
```

#### DeleteLiveUpdate

This event is called when a LiveUpdate is deleted, which sends a json message containing the **ID** of deleted LiveUpdate.

```json
{
  "ID": number
}
```

#### DeleteAllLiveUpdates

This event is called when all of the LiveUpdates are deleted. This event does not send a message.

