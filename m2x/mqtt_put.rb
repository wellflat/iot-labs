#!/usr/bin/env ruby

require "json"
require "time"
require "mqtt"
require "securerandom"
require "yaml"

config = YAML.load_file("m2x.yml")
api_key = config["api_key"]
device_id = config["device_id"]
mqtt_host = config["mqtt_host"]
stream = config["stream"][0]
temp = 25.0
broker_url = "mqtt://#{api_key}:@#{mqtt_host}"
user_agent = "M2X-Demo-Client/0.0.1"

MQTT::Client.connect(broker_url) do |client|
  client.subscribe("m2x/#{api_key}/responses")

  request = {
    id: SecureRandom.hex,
    method: "PUT",
    resource: "/v2/devices/#{device_id}/streams/#{stream}/value",
    agent: user_agent,
    body: {
      value: temp
    }
  }

  puts "Pushing value #{temp} to stream #{device_id}/#{stream}..."
  
  client.publish("m2x/#{api_key}/requests", request.to_json)
  
  response = client.get_packet
  
  puts JSON.pretty_generate(JSON.parse(response.payload))
end

     
