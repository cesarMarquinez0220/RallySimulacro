package com.rally.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;

import com.rally.demo.model.Empleado;
import com.rally.demo.repository.EmpleadoRepository;

import jakarta.validation.Valid;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;



@RestController
@RequestMapping("/api")
public class EmpleadoController {
    @Autowired
    private EmpleadoRepository repository;

    @GetMapping("/empleados")
    public List<Empleado> obtenerTodos() {
        return repository.findAll();
    }

    @GetMapping("/empleados/{departamento}")
    public List<Empleado> obtenerPorDepartamento(
            @PathVariable String departamento) {

        return repository.findByDepartamento(departamento);
    }
    
    @PostMapping("/insertar/empleados")
    public Empleado postMethodName(@Valid @RequestBody Empleado nuEmpleado) {
        
        
        return repository.save(nuEmpleado);
    }
    
    


}
