---
audio: false
generated: true
lang: es
layout: post
title: Programa en C para Decodificar un Paquete UDP
translated: true
type: note
---

Aquí tienes un ejemplo de cómo decodificar un paquete UDP en C. Este código demuestra cómo recibir un paquete UDP y extraer sus componentes clave:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

// Estructura del encabezado UDP
struct udp_header {
    uint16_t source_port;      // Puerto origen
    uint16_t dest_port;       // Puerto destino
    uint16_t length;          // Longitud del paquete UDP (encabezado + datos)
    uint16_t checksum;        // Checksum
};

void decode_udp_packet(unsigned char* buffer, int size) {
    // Asumiendo que el encabezado IP es de 20 bytes (sin opciones)
    struct udp_header* udp = (struct udp_header*)(buffer + 20);
    
    printf("\nUDP Header\n");
    printf("Source Port: %u\n", ntohs(udp->source_port));
    printf("Destination Port: %u\n", ntohs(udp->dest_port));
    printf("Length: %u\n", ntohs(udp->length));
    printf("Checksum: 0x%04x\n", ntohs(udp->checksum));
    
    // Calcular longitud de datos y puntero
    int udp_header_size = 8;  // El encabezado UDP es de 8 bytes
    int data_length = ntohs(udp->length) - udp_header_size;
    unsigned char* data = buffer + 20 + udp_header_size;
    
    printf("Data: ");
    for(int i = 0; i < data_length && i < 20; i++) {  // Imprimir máximo primeros 20 bytes
        printf("%02x ", data[i]);
    }
    printf("\n");
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    unsigned char buffer[65535];  // Tamaño máximo de paquete UDP
    
    // Crear socket UDP
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sockfd < 0) {
        perror("Socket creation failed");
        return 1;
    }
    
    // Inicializar dirección del servidor
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(12345);  // Puerto de ejemplo
    
    // Vincular socket
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(sockfd);
        return 1;
    }
    
    printf("Listening for UDP packets on port 12345...\n");
    
    while (1) {
        socklen_t client_len = sizeof(client_addr);
        int received_bytes = recvfrom(sockfd, buffer, sizeof(buffer), 0,
                                    (struct sockaddr*)&client_addr, &client_len);
                                    
        if (received_bytes < 0) {
            perror("Receive failed");
            continue;
        }
        
        decode_udp_packet(buffer, received_bytes);
    }
    
    close(sockfd);
    return 0;
}
```

Este código hace lo siguiente:

1. Define una estructura `udp_header` que coincide con el formato del encabezado del paquete UDP:
   - Puerto origen (16 bits)
   - Puerto destino (16 bits)
   - Longitud (16 bits)
   - Checksum (16 bits)

2. Crea un socket UDP y lo vincula al puerto 12345 (puedes cambiar este número de puerto).

3. La función `decode_udp_packet`:
   - Toma un búfer de paquete crudo como entrada
   - Asume que un encabezado IP de 20 bytes precede al encabezado UDP (Nota: esto puede variar si hay opciones IP presentes)
   - Extrae y convierte los campos del encabezado del orden de bytes de red (big-endian) al orden de bytes del host usando `ntohs`
   - Imprime la información del encabezado
   - Extrae y muestra los datos de payload

Para compilar y ejecutar:
```bash
gcc udp_decoder.c -o udp_decoder
sudo ./udp_decoder  # Necesita sudo por el uso de socket crudo
```

Notas importantes:
1. Este es un ejemplo básico - las aplicaciones del mundo real podrían necesitar:
   - Verificación de errores para el tamaño del paquete
   - Manejo de opciones del encabezado IP (longitud variable)
   - Verificación del checksum
   - Procesamiento de datos más sofisticado

2. Para probarlo, puedes:
   - Enviar paquetes UDP usando netcat: `echo "test" | nc -u 127.0.0.1 12345`
   - Usar una herramienta generadora de paquetes

3. El código asume que el paquete incluye un encabezado IP. Si estás trabajando con datos UDP crudos, elimina el desplazamiento +20.

4. Para uso en producción, añade más manejo de errores y posiblemente usa `struct udphdr` de `<netinet/udp.h>` en lugar de una estructura personalizada.

¿Te gustaría que explique alguna parte específica con más detalle o muestre una variación de este código?