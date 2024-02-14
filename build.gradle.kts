import org.openapitools.generator.gradle.plugin.tasks.GenerateTask

plugins {
    alias(libs.plugins.openapi.generator) apply true
}

tasks {
    register("generatePython", GenerateTask::class) {
        generatorName.set("python")
        inputSpec.set("${rootDir}/openapi.yaml")
        outputDir.set("${rootDir}/build/")
    }
}
