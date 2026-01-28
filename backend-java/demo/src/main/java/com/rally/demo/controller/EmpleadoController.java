package com.rally.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;

import com.rally.demo.model.Empleado;
import com.rally.demo.repository.EmpleadoRepository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;


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
    
    


}
