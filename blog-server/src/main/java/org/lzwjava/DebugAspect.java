package org.lzwjava;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

@Aspect
@Component
public final class DebugAspect {
    private static final Logger log = LoggerFactory.getLogger(DebugAspect.class);

    @Before("execution(* org.lzwjava...*(..))")
    public void logBefore(JoinPoint joinPoint) {
        log.info("Method executed: {}", joinPoint.getSignature());
    }

    @AfterReturning(pointcut = "execution(* org.lzwjava...*(..))", returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        log.info("Method {} returned: {}", joinPoint.getSignature(), result);
    }
}
