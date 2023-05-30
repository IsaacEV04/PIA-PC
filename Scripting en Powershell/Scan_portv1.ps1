#DATOS
#Nombre: Jesús Israel Bolaños Uvalle
#Matrícula: 2005587


# Determinando el gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando tu gateway ..."
Write-Host "Tu gateway: $subred"

#Determinando rango de subred

$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host "== Determinando tu rango de subred ..."
echo $rango

## Determinando si $ranfo termina en "."
## En ocasiones el rango de subred no termina en punto, necesitamos forzarlo.

$punto = $rango.EndsWith('.')
if ( $punto -like "False")
{
	$rango = $rango + '.' #agregamos el punto en caso que no estuviera
}

##Definimos un array con puertos a escanear.
##Establecemos una variable para Waittime

$portstoscan = @(0..10000)
$waittime = 100

##Solicitamos dirección ip a escabear:

Write-Host "Dirección ip a escanear: " -NoNewline
$direccion = Read-Host

##Generamos bucle foreach para evaluar cada puerto en $portstoscan

foreach ( $p in $portstoscan )
{
	$TCPObject = new-object System.Net.Sockets.TcpClient
		try{ $resultado = $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
		if ( $resultado -eq "True" )
		{
		Write-Host " Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
		}
}
