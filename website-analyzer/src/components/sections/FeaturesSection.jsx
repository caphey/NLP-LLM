import { BarChart2, Activity, Zap } from 'lucide-react'
import FeatureCard from '../ui/FeatureCard'

const FeaturesSection = () => {
  const features = [
    {
      icon: <BarChart2 />,
      title: "Analyse approfondie",
      description: "Évaluation complète de votre site avec des métriques détaillées",
    },
    {
      icon: <Activity />,
      title: "Performance & SEO",
      description: "Optimisation technique et visibilité dans les moteurs de recherche",
    },
    {
      icon: <Zap />,
      title: "IA & Machine Learning",
      description: "Algorithmes avancés pour des recommandations personnalisées",
    }
  ]

  return (
    <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto mb-16">
      {features.map((feature, index) => (
        <FeatureCard key={index} {...feature} />
      ))}
    </div>
  )
}

export default FeaturesSection