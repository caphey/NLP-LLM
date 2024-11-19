const TechnologiesSection = () => {
  const technologies = ['Python', 'Ollama', 'ViteJs', 'Llama']

  return (
    <div className="text-center text-indigo-200">
      <h3 className="text-xl font-semibold mb-6">Technologies utilisées</h3>
      <div className="flex justify-center gap-8 items-center">
        {technologies.map((tech, index) => (
          <div 
            key={index}
            className="bg-white/5 backdrop-blur-lg px-6 py-3 rounded-xl border border-white/10"
          >
            {tech}
          </div>
        ))}
      </div>
    </div>
  )
}

export default TechnologiesSection