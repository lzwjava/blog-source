---
audio: false
generated: true
lang: es
layout: post
title: Errores de Angular
translated: true
type: note
---

Al trabajar con Angular, los desarrolladores suelen encontrar excepciones y errores específicos. A continuación se presenta una lista categorizada de problemas comunes, sus causas y soluciones:

---

### **Errores de Plantilla y Data Binding**
1. **`ExpressionChangedAfterItHasBeenCheckedError`**  
   - **Causa**: Cambiar datos del componente después del ciclo de detección de cambios de Angular (ej., en `ngAfterViewInit` o `ngOnChanges`).  
   - **Solución**: Usar `ChangeDetectorRef.detectChanges()` o asegurarse de que los cambios de datos ocurran antes de que la detección de cambios finalice.

2. **`Cannot read property 'X' of undefined`**  
   - **Causa**: Acceder a propiedades de objetos no inicializados en plantillas (ej., `{{ user.name }}` cuando `user` es `null`).  
   - **Solución**: Usar el operador de navegación segura (`{{ user?.name }}`) o inicializar los objetos correctamente.

3. **`Can't bind to 'X' since it isn't a known property of 'Y'`**  
   - **Causa**: Falta la declaración del componente/directiva o error tipográfico en el nombre de la propiedad.  
   - **Solución**: Importar la directiva/componente en el módulo o revisar si hay errores tipográficos.

---

### **Errores de Inyección de Dependencias (DI)**
4. **`NullInjectorError: No provider for XService`**  
   - **Causa**: Servicio no provisto en el módulo/componente o dependencia circular.  
   - **Solución**: Agregar el servicio al array `providers` del módulo/componente.

5. **`No value accessor for form control`**  
   - **Causa**: Control de formulario personalizado sin la implementación de `ControlValueAccessor` o enlace incorrecto de `formControlName`.  
   - **Solución**: Implementar `ControlValueAccessor` para controles personalizados o revisar los enlaces del formulario.

---

### **Errores de TypeScript y Build**
6. **`Type 'X' is not assignable to type 'Y'`**  
   - **Causa**: Discrepancias de tipos (ej., tipo de dato incorrecto pasado a un componente).  
   - **Solución**: Asegurarse de que los tipos coincidan o usar aserciones de tipo (si es intencional).

7. **`ERROR in Cannot find module 'X'`**  
   - **Causa**: Falta un paquete npm o ruta de importación incorrecta.  
   - **Solución**: Instalar el paquete (`npm install X`) o corregir la ruta de importación.

---

### **Errores de Componente y Módulo**
8. **`Component is not part of any NgModule`**  
   - **Causa**: Componente no declarado en un módulo o módulo no importado.  
   - **Solución**: Agregar el componente a `declarations` en su módulo o importar el módulo.

9. **`ViewDestroyedError: Attempt to use a destroyed view`**  
   - **Causa**: Suscripciones u operaciones asíncronas ejecutándose después de la destrucción del componente.  
   - **Solución**: Darse de baja en `ngOnDestroy` o usar la pipe `async`.

---

### **Errores HTTP y de API**
10. **`HttpClient provider not found`**  
    - **Causa**: Falta la importación de `HttpClientModule` en el módulo.  
    - **Solución**: Importar `HttpClientModule` en `AppModule`.

11. **Problemas de CORS**  
    - **Causa**: El backend no permite solicitudes desde el origen del frontend.  
    - **Solución**: Configurar CORS en el servidor o usar un proxy en Angular (`proxy.conf.json`).

---

### **Errores de Routing**
12. **`Route not found`**  
    - **Causa**: Definición de ruta incorrecta o falta un módulo de carga diferida (lazy-loaded).  
    - **Solución**: Revisar las rutas y la sintaxis de carga diferida (`loadChildren: () => import(...)`).

---

### **Errores de Formularios**
13. **`FormControl not found`**  
    - **Causa**: Usar `formControlName` sin envolverlo en un `[formGroup]`.  
    - **Solución**: Asegurarse de que el form group padre esté inicializado y enlazado.

---

### **Misceláneos**
14. **`Maximum call stack size exceeded`**  
    - **Causa**: Funciones recursivas o dependencias circulares.  
    - **Solución**: Refactorizar el código para eliminar la recursividad/referencias circulares.

15. **`Zone.js Promise rejection`**  
    - **Causa**: Rechazos de promesas no manejados.  
    - **Solución**: Agregar `.catch()` o usar `try/catch` con `async/await`.

16. **Errores de Compilación AOT**  
    - **Causa**: Sintaxis de plantilla incompatible con la compilación Ahead-of-Time.  
    - **Solución**: Evitar expresiones complejas en plantillas o usar sintaxis compatible con Angular.

---

### **Buenas Prácticas para Evitar Errores**
- Usar la pipe `async` para observables y que se desuscriba automáticamente.
- Activar las comprobaciones estrictas de TypeScript (`strict: true` en `tsconfig.json`).
- Ejecutar `ng lint` para detectar problemas de calidad de código.
- Probar con la bandera `--prod` para simular builds AOT.

Al abordar estos problemas comunes de manera metódica, puedes agilizar el desarrollo con Angular y reducir el tiempo de depuración.