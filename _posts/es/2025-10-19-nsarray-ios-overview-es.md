---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de NSArray para el Desarrollo en iOS
translated: true
type: note
---

### ¿Qué es NSArray?

`NSArray` es una clase en el framework Foundation de Apple, parte del SDK de iOS (y macOS, etc.). Representa una colección ordenada e inmutable de objetos, similar a un array en otros lenguajes. Esto significa que una vez que creas un `NSArray`, no puedes añadir, eliminar o reemplazar elementos—solo puedes leerlo. Se usa comúnmente en Objective-C para el desarrollo de aplicaciones iOS para almacenar y gestionar listas de datos, como preferencias de usuario, resultados de consultas de bases de datos o elementos de UI.

Características clave:
- **Inmutable**: Tamaño y contenido fijos después de la creación (usa `NSMutableArray` para versiones mutables).
- **Type-safe para objetos**: Almacena punteros a objetos Objective-C (ej., `NSString`, `NSNumber`, clases personalizadas). No admite primitivos directamente—envuélvelos en `NSNumber` o similar.
- **Acceso indexado**: Los elementos se acceden por índice entero (base 0).
- **Thread-safe**: Generalmente seguro para lecturas concurrentes, pero no para escrituras (dado que es inmutable).
- **Integración**: Funciona perfectamente con otras clases de Foundation como `NSDictionary`, `NSString` y los componentes de UI de Cocoa Touch.

En Swift, `NSArray` se vincula a `Array`, pero si trabajas en Objective-C (común en código iOS heredado), usarás `NSArray` directamente.

### Cómo usar NSArray en iOS

Para usar `NSArray` en un proyecto de iOS:
1. Importa el framework Foundation (normalmente se incluye por defecto en las apps de iOS).
   ```objc
   #import <Foundation/Foundation.h>
   ```

2. **Crear un NSArray**:
   - Sintaxis literal (iOS 6+): `@[objeto1, objeto2, ...]`
   - Método init: `[[NSArray alloc] initWithObjects:objeto1, objeto2, nil]`
   - Desde un array C: `initWithArray:copyItems:`

   Ejemplo:
   ```objc
   NSArray *frutas = @[@"manzana", @"plátano", @"cereza"];
   // O:
   NSArray *numeros = [[NSArray alloc] initWithObjects:@1, @2, @3, nil];
   ```

3. **Acceder a Elementos**:
   - `objectAtIndex:` para obtener un elemento.
   - `count` para la longitud.
   - `firstObject` / `lastObject` para los extremos.
   - `containsObject:` para comprobar existencia.

   Ejemplo:
   ```objc
   NSString *primeraFruta = [frutas objectAtIndex:0]; // "manzana"
   NSUInteger cantidad = [frutas count]; // 3
   BOOL tieneNaranja = [frutas containsObject:@"naranja"]; // NO
   ```

4. **Iterar**:
   - Enumeración rápida: `for (id obj in array) { ... }`
   - `enumerateObjectsUsingBlock:` para iteración basada en bloques (iOS 4+).

   Ejemplo:
   ```objc
   for (NSString *fruta in frutas) {
       NSLog(@"Fruta: %@", fruta);
   }
   ```

5. **Operaciones Comunes**:
   - Ordenar: `sortedArrayUsingSelector:` o `sortedArrayUsingComparator:`.
   - Filtrar: `filteredArrayUsingPredicate:` (con NSPredicate).
   - Unir: `componentsJoinedByString:` para strings.
   - Escribir en archivo: `writeToFile:atomically:`.

   Ejemplo (filtrando):
   ```objc
   NSPredicate *predicado = [NSPredicate predicateWithFormat:@"length > 5"];
   NSArray *frutasLargas = [frutas filteredArrayUsingPredicate:predicado];
   // Resultados: @[@"plátano", @"cereza"]
   ```

6. **En Contextos de iOS**:
   - **Table Views**: Pasa un `NSArray` a los métodos de data source de `UITableView` como `tableView:numberOfRowsInSection:` (vía `count`) y `tableView:cellForRowAtIndexPath:` (vía `objectAtIndex:`).
   - **User Defaults**: Almacena/recupera con `NSUserDefaults`: `[defaults setObject:array forKey:@"savedItems"];`.
   - **Manejo de JSON**: Convierte a/desde `NSData` con `JSONObjectWithData:options:error:`.

Para necesidades mutables (ej., añadir elementos dinámicamente), cambia a `NSMutableArray`:
```objc
NSMutableArray *frutasMutables = [NSMutableArray arrayWithArray:frutas];
[frutasMutables addObject:@"dátil"];
```

### Consejos
- Siempre verifica `nil` o los límites para evitar cierres inesperados: Usa `objectAtIndex:` con validación de índice.
- Rendimiento: O(1) para acceso, O(n) para búsquedas.
- iOS Moderno: Considera el `Array` de Swift para nuevos proyectos—es más type-safe.

[Documentación de NSArray](https://developer.apple.com/documentation/foundation/nsarray)  
[Documentación de NSMutableArray](https://developer.apple.com/documentation/foundation/nsmutablearray)