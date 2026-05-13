export default function AIDJOperationalDashboard() {
  const kpis = [
    { label: "Post-Session Search Rate", value: "34.1%", change: "+8.2%", status: "Elevated" },
    { label: "Recommendation Override Rate", value: "27.6%", change: "+5.4%", status: "Watch" },
    { label: "Prompt Reformulation Rate", value: "22.8%", change: "+4.1%", status: "Rising" },
    { label: "28-Day Retention", value: "61.2%", change: "-2.3%", status: "Slight Decline" },
  ];

  const alerts = [
    "Post-session search rate is above baseline for AI DJ treatment users.",
    "Recommendation override behavior increased among exploratory listeners.",
    "Prompt reformulation rate is trending upward across mood-based requests.",
    "Recommendation diversity declined across repeated exposure cycles.",
  ];

  const actions = [
    {
      signal: "Emotionally different searches",
      action: "Improve mood and energy calibration",
      metric: "Lower mood-shift search rate",
    },
    {
      signal: "Artist-specific recovery searches",
      action: "Strengthen familiar-to-adjacent artist pathways",
      metric: "Lower artist recovery search rate",
    },
    {
      signal: "Repeated prompt reformulation",
      action: "Improve prompt parsing and retrieval matching",
      metric: "Lower reformulation rate",
    },
  ];

  return (
    <main className="min-h-screen bg-slate-950 text-white p-8">
      <section className="max-w-7xl mx-auto space-y-8">
        <header>
          <p className="text-sm uppercase tracking-[0.3em] text-green-400">
            Mock Product Analytics Dashboard
          </p>
          <h1 className="mt-3 text-4xl md:text-5xl font-bold">
            AI DJ Operational Monitoring
          </h1>
          <p className="mt-4 max-w-4xl text-slate-300 text-lg">
            A mock internal dashboard showing how behavioral evaluation signals from a
            synthetic AI DJ recommendation-system dataset could be translated into
            ongoing feature-health monitoring, product alerts, and next-test metrics.
          </p>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-5">
          {kpis.map((kpi) => (
            <div
              key={kpi.label}
              className="rounded-3xl border border-slate-800 bg-slate-900 p-6 shadow-xl"
            >
              <p className="text-sm text-slate-400">{kpi.label}</p>
              <div className="mt-4 flex items-end justify-between">
                <h2 className="text-4xl font-bold">{kpi.value}</h2>
                <span className="text-sm font-semibold text-green-400">
                  {kpi.change}
                </span>
              </div>
              <p className="mt-3 text-xs uppercase tracking-wide text-slate-500">
                {kpi.status}
              </p>
            </div>
          ))}
        </section>

        <section className="grid grid-cols-1 xl:grid-cols-3 gap-6">
          <div className="xl:col-span-2 rounded-3xl border border-slate-800 bg-slate-900 p-6">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-semibold">Behavioral Signal Monitoring</h2>
              <span className="text-sm text-slate-400">28-day synthetic window</span>
            </div>

            <div className="space-y-6">
              <MetricBar label="Post-session search lift" value="+22.4 pp" width="78%" />
              <MetricBar label="Recommendation override lift" value="+13.4 pp" width="61%" />
              <MetricBar label="Prompt reformulation lift" value="+11.5 pp" width="55%" />
              <MetricBar label="Recommendation diversity decline" value="-8.1%" width="44%" />
            </div>
          </div>

          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-2xl font-semibold mb-5">Monitoring Alerts</h2>
            <div className="space-y-4">
              {alerts.map((alert) => (
                <div
                  key={alert}
                  className="rounded-2xl border border-slate-800 bg-slate-950 p-4"
                >
                  <p className="text-sm text-slate-300">{alert}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-2xl font-semibold mb-6">
            Evaluation Signals → Product Actions → Success Metrics
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {actions.map((item) => (
              <div
                key={item.signal}
                className="rounded-2xl border border-slate-800 bg-slate-950 p-5"
              >
                <p className="text-xs uppercase tracking-wide text-slate-500">
                  Observed Signal
                </p>
                <h3 className="mt-1 text-lg font-semibold">{item.signal}</h3>

                <p className="mt-5 text-xs uppercase tracking-wide text-slate-500">
                  Suggested Product Action
                </p>
                <p className="mt-1 font-semibold text-green-400">{item.action}</p>

                <p className="mt-5 text-xs uppercase tracking-wide text-slate-500">
                  Next Test Metric
                </p>
                <p className="mt-1 font-semibold text-cyan-400">{item.metric}</p>
              </div>
            ))}
          </div>
        </section>
      </section>
    </main>
  );
}

function MetricBar({ label, value, width }) {
  return (
    <div>
      <div className="flex justify-between text-sm mb-2">
        <span className="text-slate-300">{label}</span>
        <span className="font-semibold text-green-400">{value}</span>
      </div>
      <div className="h-3 w-full rounded-full bg-slate-800">
        <div className="h-3 rounded-full bg-green-400" style={{ width }} />
      </div>
    </div>
  );
}
