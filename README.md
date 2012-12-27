##STARTING THE SERVER
#Basic mode with one node
java -jar selenium-server-standalone-2.14.0.jar

#With hubs
Hub: java -jar selenium-server-standalone-2.14.0.jar -role hub <br/>
Nodes: java -jar selenium-server-standalone-2.14.0.jar -role node  -hub http://localhost:4444/grid/register
