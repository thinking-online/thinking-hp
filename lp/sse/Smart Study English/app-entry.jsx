/* Smart Study English — App entry */

function App() {
  return (
    <>
      <Hero />
      <BrainCompareSection />
      <SelfCheckSection />
      <WhySection />
      <OrderSection />
      <MethodSection />
      <DaysSection />
      <ResultsSection />
      <VoicesSection />
      <MediaSection />
      <MessageSection />
      <GuaranteeSection />
      <NotForSection />
      <FAQSection />
      <PriceSection />
      <FinalSection />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
