package com.rally.demo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.rally.demo.model.Empleado;

public interface EmpleadoRepository extends JpaRepository<Empleado, Long>{
    List<Empleado> findByDepartamento(String departamento);
}
